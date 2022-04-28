import random

class Questions:
    def __init__(self,filename):
        self.filename=filename
        self.row=0
        
    def get_question(self):
        f = open(self.filename, "r")
        st=f.read()
        st=st.split('\n')
        q_no=random.randint(0,len(st)-1)
        self.row=q_no
        
        ques=""
        for i in st[q_no]:
            if i!=':':
                ques+=i
            else:
                break
                
        return ques
    
    def get_answer(self):
        f = open(self.filename, "r")
        st=f.read()
        st=st.split('\n')

        ans=st[self.row]
        ans=ans.split(':')
        
        break_con=0
        ans_str=""
        for i in ans[1]:
            if break_con==0 and i!=' ':
                break_con=1
            if break_con==1:
                ans_str+=i
                
        return ans_str
