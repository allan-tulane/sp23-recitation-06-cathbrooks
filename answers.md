# CMPS 2200 Recitation 6
## Answers

**Name:**___Catherine Brooks______________________
**Name:**___David Webster



Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt         | 1340    |  826      |  0.62  |
alice29.txt    | 1268622 |  676374   |  0.53  |
asyoulik.txt   | 1032252 |  606448   |  0.59  |
grammar.lsp    | 32438   |  17356    |  0.54  |
fields.c       | 105778  |  56206    |  0.53  |

We can see here that pretty consistently, huffman coding cost is about half the fixed-length coding cost.


- **e.**
if every character has the same frequency then the huffman tree would be balanced, with each letter's encoding being the same bit length.
Which means each character would cost log2(# of characters), we then want to multiply by the frequency. however since each character has the same length encoding the cost would be the total number of characters multiplied by log2(# of characters). It would be conistent across all documents with similar total characters and same alphabet. 
  

