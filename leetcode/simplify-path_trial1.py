class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        st = []
        for d in dirs:
            if not d or d == '.':
                continue
            if d == '..':
                if st:
                    st.pop()
            else:
                st.append('/'+d)
        return ''.join(st) if st else '/'