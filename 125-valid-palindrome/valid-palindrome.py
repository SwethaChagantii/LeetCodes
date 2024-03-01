class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for ch in s:
            if ch.isdigit() or ch.isalpha():
                st += ch
        print(st)
        rev_str = st[::-1]
        if st.lower() == rev_str.lower():
            return True
        return False
