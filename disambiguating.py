import torch
from typing import List, Optional, Tuple, Dict

def resolve_collision(tokens: List[str]) -> List[int]:
    indices = []
    for i in range(len(tokens)):
        for j in range(len(tokens)):
            if i == j:
                continue
            if tokens[j].startswith(tokens[i]):
                break
        else:
            indices.append(i)
    return indices

def disambiguate_1(tokenizer, indices, probs):
    """
    去除有共享前缀的标记
    """
    candidate_tokens = tokenizer.convert_ids_to_tokens(indices)
    new_candidate_indices_idx = resolve_collision(candidate_tokens)
    new_candidate_indices = indices

    new_candidate_probs = probs
    for i in range(len(new_candidate_probs)):
        if i not in new_candidate_indices_idx:
            new_candidate_probs[i] = 0

    return new_candidate_indices, new_candidate_probs, new_candidate_indices_idx

def construct_grouped_distribution(candidate_tokens_list, probs, indices):

    sorted_data = sorted(zip(candidate_tokens_list, probs, indices), key=lambda x: x[0], reverse=False)
    # candidate_tokens_list, probs, indices = zip(*sorted_data)

    grouped_tokens = []
    grouped_probs = []
    grouped_indices = []
    
    prev_token, group_prob, group_indices = sorted_data[0]
    group_prob = [group_prob]
    group_indices = [group_indices]
    
    for token, prob, index in sorted_data[1:]:
        if token.startswith(prev_token):
            # 当前token与前一个token有共同前缀
            group_prob.append(prob)
            group_indices.append(index)
        else:
            # 当前token与前一个token没有共同前缀
            if prev_token != '':
                # 将之前的group添加到结果中
                grouped_tokens.append(prev_token)
                grouped_probs.append(group_prob)
                grouped_indices.append(group_indices)
            
            # 重置group
            prev_token = token
            group_prob = [prob]
            group_indices = [index]
    
    # 添加最后一个group
    grouped_tokens.append(prev_token)
    grouped_probs.append(group_prob)
    grouped_indices.append(group_indices)

    return grouped_tokens, grouped_probs, grouped_indices
