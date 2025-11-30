class tool:
    def ToExist(self, UsernameList,Username):
        i = 0
        Status = False
        while i < len(UsernameList):
            if Username == UsernameList[i]:
                Status = True
                break
            i += 1
        return Status
