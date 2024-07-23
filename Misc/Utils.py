class Base62:
    # Define the base62 character set
    CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    @classmethod
    def encode(cls, num):
        """Encodes an integer to a base62 string."""
        if num == 0:
            return cls.CHARSET[0]
        
        base62 = []
        base = len(cls.CHARSET)
        
        while num:
            num, remainder = divmod(num, base)
            base62.append(cls.CHARSET[remainder])
        
        return ''.join(reversed(base62))

    @classmethod
    def decode(cls, base62):
        """Decodes a base62 string to an integer."""
        base = len(cls.CHARSET)
        num = 0
        
        for char in base62:
            num = num * base + cls.CHARSET.index(char)
        
        return num


def __main__():
    # Example usage:
    number = 125
    encoded = Base62.encode(number)
    print(f"Encoded {number} to base62: {encoded}")

    decoded = Base62.decode(encoded)
    print(f"Decoded {encoded} back to: {decoded}")


if __name__ == '__main__':
    __main__()