# Provably Secure Disambiguating Neural Linguistic Steganography

This repository contains the implementation of a provably secure disambiguating steganography method based on grouping ambiguous pools and synchronous sampling.

Note: The code will be released upon acceptance of the paper.

## Overview
Recent research in provably secure neural linguistic steganography has overlooked a crucial aspect: the sender must detokenize stegotexts to avoid raising suspicion from the eavesdropper. The segmentation ambiguity problem, which arises when using subword models, leads to occasional decoding failures in all neural language steganography implementations based on these models. Current solutions to this issue involve altering the probability distribution of candidate words, rendering them incompatible with provably secure steganography. In this paper, we introduce a novel grouped sampling approach that effectively addresses the segmentation ambiguity problem. We experimentally demonstrate the applicability of our solution to various models and provably secure steganography methods, showcasing its potential to significantly improve the reliability and security of neural linguistic steganography systems.

## Citation
Please cite it if you find the repository helpful.
