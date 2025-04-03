def sha256_hash(input_str:str) -> str:
    # Define constantes importantes
    blocks_bits_size = 512
    words_per_block = 16
    words_bits_size = 32

    # Codifica a entrada usando utf-8
    input_str = input_str.encode('utf-8')

    # Gera uma cadeia de caracteres com todos os bits da entrada
    input_str = ''.join(f'{byte:08b}' for byte in input_str)

    # Obtém o tamanho da entrada original (em bits)
    input_bits_size = len(input_str)

    # Adiciona o bit 1 (como "string") à entrada
    input_str += '1'

    # Calcula a quantidade de preenchimento necessário
    pad_quant = (448 - len(input_str) % blocks_bits_size) % blocks_bits_size

    # Aplica o preenchimento
    input_str += pad_quant * '0'

    # Coloca o tamanho da entrada original (em bits) nos últimos 64 bits da mensagem original já preenchida
    input_str += f'{input_bits_size:064b}'

    # Gera os blocos de 512 bits
    blocks = [f'{input_str[i:i + blocks_bits_size]}' for i in range(0, len(input_str), blocks_bits_size)]

    # Gera as 16 palavras de 32 bits para cada bloco
    blocks = [[int(input_str[i:i +  words_bits_size], 2) for i in range(0, blocks_bits_size, words_bits_size)] for block in blocks]

    # Expande para as 64 palavras
    for block in blocks:
        for i in range(16, 64):
            # Gera uma nova palavra de 32 bits
            new_word = (lsigma1(block[i - 2]) + block[i - 7] + lsigma0(block[i - 15]) + block[i - 16]) & 0xFFFFFFFF
            block.append(new_word)

    # Inicializando os 8 registradores
    registers = [
        0x6a09e667,
        0xbb67ae85,
        0x3c6ef372,
        0xa54ff53a,
        0x510e527f,
        0x9b05688c,
        0x1f83d9ab,
        0x5be0cd19
    ]

    # Inicializa as variáveis temporárias
    a, b , c, d, e, f, g, h = registers

def rotr(n:int, word:int):
    return (word >> n) | (word << (32 - n))

def shr(n:int, word:int) -> int:
    return word >> n

def lsigma0(word:int) -> int:
    return rotr(7, word) ^ rotr(18, word) ^ shr(3, word)

def lsigma1(word: int) -> int:
    return rotr(17, word) ^ rotr(19, word) ^ shr(10, word)

def sigma4(word:int) -> int:
    return rotr(6, word) ^ rotr(11, word) ^ rotr(25, word)

def choice(x:int, y:int, z:int):
    return (x & y) ^ (~x & z)

def majority(x:int, y:int, z:int):
    return (x & y) ^ (x & z) ^ (y & z)