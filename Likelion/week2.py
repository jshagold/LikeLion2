#-*- coding:utf-8 -*-

# 작성자 정성학

# 점수를 입력받습니다
fir_subj = float(input('첫번째 과목 입력:'))
sec_subj = float(input('두번째 과목 입력:'))
trd_subj = float(input('세번째 과목 입력:'))
four_subj = float(input('네번째 과목 입력:'))

# 입력받은 점수를 평균냅니다
ave = (fir_subj+sec_subj+trd_subj+four_subj)/4


# 결과 출력입니다
if fir_subj < 50 or sec_subj < 50 or trd_subj < 50 or four_subj < 50:
    print('평균점수는 '+str(round(ave,1))+'점 입니다.\n'+'과락으로 불합격입니다.')
elif ave < 60:
    print('평균점수는 '+str(round(ave,1))+'점 입니다.\n'+'평균미달으로 불합격임미다.')
else:
    print('평균점수는 '+str(round(ave,1))+'점 입니다.\n'+'모든 과목이 50점이상이고 합격입니다.')

