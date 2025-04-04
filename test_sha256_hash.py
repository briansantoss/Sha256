import pytest
import sha256

test_cases = [
    # Testa string vazia
    ('', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'),
    ('abc', 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'),
    # Testa entradas mais longas
    ('a'* 64, 'ffe054fe7ae0cb6dc65c3af9b61d5209f439851db43d0ba5997337df154668eb'),
    ('a'*1000, '41edece42d63e8d9bf515a9ba6932e1c20cbc9f5a5d134645adb5db1b9737ea3'),
    # Testa entradas semelhantes
    ('The quick brown fox jumps over the lazy dog', 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'),
    ('The quick brown fox jumps over the lazy dog.', 'ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c'),
    # Testa entrada com símbolos especiais e "emojis"
    ('@#$_!', 'e3c3c475fc0c7da3e1c41df0726df5571d2cead1adc46d9fc2c4a327d39b8f4c'),
    ('🔥🚀💻', '4bb39d1c4b46ded8e30b71294605a11328500d2ac5be801e5d96b289b616b39d'),
    ('Olá, mundo!', '9583b013baa520d3a893c4270d0c67732d7ef1768eb0a13533b4e7b134d4b131'),
    # Testa string numérica
    ('1234567890', 'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646'),
    # Testa entrada com espaços
    (' a b c ', '21ddd8484ea4c9a7eb6ad01896156e9ab8a04f222b0d1caedc561a611812d38e')
]

@pytest.mark.parametrize('input_str, expected', test_cases)
def test_hash(input_str, expected):
    res_hash = sha256.sha256_hash(input_str)
    assert res_hash == expected, f'Error in hashing: {input_str}'