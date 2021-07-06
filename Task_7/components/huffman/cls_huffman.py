class cls_huffman:
    def __init__(self, inpt_text: str) -> None:
        self._text = inpt_text

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text

    def fn_frequency(self) -> dict[str, int]:
        frequency: dict[str, int] = {}
        for letter in self.text:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        return frequency

    def fn_frequency_key(self) -> dict[int, list[tuple[str, int]]]:
        dct_frequency: dict[int, list[tuple[str, int]]] = {}
        for k, v in self.fn_frequency().items():
            if v in dct_frequency:
                dct_frequency[v].append((k, v))
            else:
                dct_frequency[v] = [(k, v)]
        return dct_frequency
