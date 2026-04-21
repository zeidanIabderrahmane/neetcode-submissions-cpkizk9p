class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        c = 0
        length = len(cleaned) -1
        while c < length:
            if cleaned[c] != cleaned[length]:
                return False
            c += 1
            length -= 1
        return True