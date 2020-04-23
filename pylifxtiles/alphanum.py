

#Module to draw letters and numbers on LIFX Tiles

alpha = {'r': [1,
  9,
  17,
  25,
  33,
  41,
  49,
  57,
  2,
  3,
  4,
  13,
  22,
  29,
  34,
  35,
  36,
  44,
  53,
  62],
 't': [1, 2, 3, 4, 5, 6, 11, 19, 27, 35, 43, 51, 59],
 's': [2, 3, 4, 5, 6, 9, 17, 26, 27, 28, 37, 46, 54, 57, 58, 59, 60, 61],
 'u': [1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49, 54, 59, 59, 60, 61],
 'v': [1, 9, 17, 25, 33, 41, 50, 5, 13, 21, 29, 37, 45, 52, 59],
 'q': [3, 4, 10, 13, 17, 22, 25, 30, 33, 38, 41, 46, 50, 53, 59, 60, 62],
 'w': [1,
  9,
  17,
  25,
  33,
  41,
  43,
  44,
  49,
  58,
  51,
  52,
  61,
  6,
  14,
  22,
  30,
  38,
  46,
  54],
 'x': [1, 6, 10, 13, 19, 20, 27, 28, 35, 36, 43, 44, 50, 53, 57, 62],
 'y': [1, 6, 10, 13, 19, 20, 27, 35, 43, 51, 59],
 'z': [1, 2, 3, 4, 5, 6, 14, 21, 28, 35, 42, 49, 57, 58, 59, 60, 61, 62],
 'a': [3,
  4,
  10,
  13,
  17,
  22,
  25,
  30,
  33,
  34,
  35,
  36,
  37,
  38,
  41,
  46,
  49,
  54,
  57,
  62],
 'b': [1,
  2,
  3,
  4,
  9,
  13,
  17,
  21,
  25,
  26,
  27,
  28,
  33,
  37,
  41,
  46,
  49,
  54,
  57,
  58,
  59,
  60,
  61],
 'c': [3, 4, 5, 6, 10, 17, 25, 33, 41, 50, 59, 60, 61, 62],
 'd': [1,
  2,
  3,
  4,
  9,
  13,
  17,
  22,
  25,
  30,
  33,
  38,
  41,
  46,
  49,
  53,
  57,
  58,
  59,
  60],
 'e': [1,
  2,
  3,
  4,
  5,
  6,
  9,
  17,
  25,
  26,
  27,
  28,
  33,
  41,
  49,
  57,
  58,
  59,
  60,
  61,
  62],
 'f': [1, 2, 3, 4, 5, 6, 9, 17, 25, 26, 27, 28, 33, 41, 49, 57],
 'g': [1,
  2,
  3,
  4,
  5,
  9,
  14,
  17,
  25,
  33,
  35,
  36,
  37,
  38,
  41,
  46,
  49,
  54,
  57,
  58,
  59,
  60,
  61],
 'h': [1,
  6,
  9,
  14,
  17,
  22,
  25,
  30,
  33,
  34,
  35,
  36,
  37,
  38,
  41,
  46,
  49,
  54,
  57,
  62],
 'i': [3, 4, 11, 12, 19, 20, 27, 28, 35, 36, 43, 44, 51, 52, 59, 60],
 'j': [1, 2, 3, 4, 5, 6, 13, 21, 29, 37, 41, 45, 49, 52, 58, 59],
 'k': [1, 5, 9, 12, 17, 19, 25, 26, 33, 35, 41, 44, 49, 53, 57, 62],
 'l': [1, 9, 17, 25, 33, 41, 49, 57, 58, 59, 60, 61, 62],
 'm': [1,
  6,
  9,
  10,
  13,
  14,
  17,
  19,
  20,
  22,
  25,
  30,
  33,
  38,
  41,
  46,
  49,
  54,
  57,
  62],
 'n': [1, 9, 17, 25, 33, 41, 49, 57, 18, 27, 36, 45, 14, 22, 30, 38, 54, 62],
 'o': [3, 4, 10, 13, 17, 22, 25, 30, 33, 38, 41, 46, 50, 53, 59, 60],
 'p': [1, 9, 17, 25, 33, 41, 49, 57, 2, 3, 4, 13, 22, 29, 34, 35, 36]}

nums = {'zero': [3, 4, 10, 13, 17, 22, 25, 30, 33, 38, 41, 46, 50, 53, 59, 60],
 'one': [3, 4, 11, 12, 19, 20, 27, 28, 35, 36, 43, 44, 51, 52, 59, 60],
 'two': [1,
  2,
  3,
  4,
  5,
  14,
  22,
  30,
  34,
  35,
  36,
  37,
  37,
  41,
  49,
  57,
  58,
  59,
  60,
  61,
  62],
 'three': [1,
  2,
  3,
  4,
  5,
  6,
  13,
  14,
  21,
  22,
  26,
  27,
  28,
  29,
  30,
  34,
  35,
  36,
  37,
  45,
  46,
  53,
  54,
  57,
  58,
  59,
  60,
  62,
  63],
 'four': [1,
  5,
  6,
  9,
  13,
  14,
  17,
  21,
  22,
  25,
  26,
  27,
  28,
  29,
  30,
  37,
  38,
  45,
  46,
  53,
  54,
  61,
  62],
 'five': [1,
  2,
  3,
  4,
  5,
  6,
  9,
  17,
  25,
  26,
  27,
  28,
  29,
  38,
  46,
  54,
  57,
  58,
  59,
  60,
  61],
 'six': [3,
  4,
  5,
  10,
  17,
  25,
  33,
  35,
  36,
  37,
  38,
  41,
  42,
  46,
  49,
  54,
  58,
  59,
  60,
  61],
 'seven': [1, 2, 3, 4, 5, 6, 14, 22, 30, 37, 44, 51, 58],
 'eight': [2,
  3,
  4,
  5,
  9,
  14,
  18,
  21,
  27,
  28,
  34,
  37,
  41,
  46,
  49,
  54,
  58,
  59,
  60,
  61],
 'nine': [3,
  4,
  10,
  13,
  17,
  22,
  25,
  30,
  34,
  35,
  36,
  37,
  38,
  46,
  54,
  59,
  60,
  61,
  63]}