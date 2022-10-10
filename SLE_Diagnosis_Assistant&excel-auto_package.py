##初始設定
##A. SLE
import numpy as np
SLE_domain = np.array([['Constitutional'], ['Hematologic'], ['Neuropsychiatric'], ['Mucocutaneous'], ['Serosal'], ['Musculoskeletal'], ['Renal'], ['Antiphospholipid antibodies'], ['Complement_proteins'], ['SLE-specific antibodies']])
# condition nparray(10*4 = 7*4 + 3*4)
SLE_ccond = np.array([['Fever', None, None, None], ['Leukopenia', 'Thrombocytopenia', 'Autoimmune hemolysis', None], ['Delirium', 'Psychosis', 'Seizure', None], ['Non-scarring alopecia', 'Oral ulcers', 'Subacute cutaneous OR discoid lupus', 'Acute cutaneous lupus'], ['Pleural or pericardial effusion', 'Acute pericarditis', None, None], ['Joint involvement',None, None, None], ['Proteinuria = ___ g/24hours by 24-hour urine?\n*Please input a positive integer or float.', 'Which class best subscribes your status of lupus nephritis according to renal biopsy?\n*Please input a integer from 0 to 6("0":Normal ; "1"-"6":Class 1-6 lupus nephritis)', None, None]])
SLE_icond = np.array([['Anti-cardiolipin antibodies OR Anti-β2GP1 antibodes OR Lupus anticoagulant', None, None, None], ['Low C3 OR low C4', 'Low C3 AND low C4', None, None],['Anti-dsDNA antibody OR Anti-Smith antibody', None, None, None]])
SLE_cond = np.vstack((SLE_ccond, SLE_icond))
# weight array
SLE_weight = np.array([[2, 0, 0, 0], [3, 4, 4, 0], [2, 3, 5, 0], [2, 2, 4, 6], [5, 6, 0, 0], [6, 0, 0, 0], [4, 8, 10, 0], [2, 0, 0, 0], [3, 4, 0, 0], [6, 0, 0, 0]])
# Ans array
SLE_ans = np.array(None, (object, [10, 4]))
# 製作問答loop_control_array(元素為各domain之condition個數) >>用於SLE各condition問答  
SLE_loop_control = np.count_nonzero(SLE_cond, axis=1)

## B. SLEDAI:  #盡量不要重複問(Fever, Thrombocytopenia, Psychosis, Seizure, Proteinuria)
#如果使用者有意願 >>> 用SLEDAI進一步嚴重度分級 / 先不做科別方類
import numpy as np
SLEDAI_cond = np.array(["Seizure(recent onset)", "Psychosis", "Organic brain syndrome", "Visual disturbance", "Cranial nerve disorder", "Lupus headache", "CVA(new onset)", "Vasculitis", "Arthritis", "Myositis", "Urinary casts", "Hematuria", "Proteinuria", "Pyuria", "Rash", "Alopecia", "Mucosal ulcers", "Pleurisy", "Pericarditis", "Low complement", "Increased DNA binding", "Fever", "Thrombocytopenia", "Leukopenia"])
SLEDAI_def = np.array(["Recent onset, exclude metabolic, infections, or drug causes.", "Altered ability to function in normal activity due to severe disturbance in the perception of reality. Exclude uremia and drug causes.", " Altered mental function with impaired orientation, memory, or other intellectual function, with rapid onset and fluctuating clinical features, inability to sustain attention to environment, plus at least 2 of the following: perceptual disturbance, incoherent speech, insomnia or daytime drowsiness, or increased or decreased psychomotor activity. Exclude metabolic, infectious, or drug causes.", "Retinal changes of SLE. Exclude hypertension, infection, or drug causes", "New onset of sensory or motor neuropathy involving cranial nerves.", "Severe, persistent headache; may be migrainous, but must be nonresponsive to narcotic analgesia.", "New onset of cerebrovascular accident(s). Exclude arteriosclerosis.", "Ulceration, gangrene, tender finger nodules, periungual infarction, splinter hemorrhages, or biopsy or angiogram proof of vasculitis.", "≥2 joints with pain and signs of inflammation (i.e., tenderness, swelling, or effusion).", "Proximal muscle aching/weakness, associated with elevated creatine phosphokinase/aldolase or electromyogram changes or a biopsy showing myositis.", "Heme-granular or red blood cell casts", ">5 red blood cells/high power field. Exclude stone, infection, or other cause.", ">0.5 gram/24 hours", ">5 white blood cells/high power field. Exclude infection.", "Inflammatory type rash", "Abnormal, patchy or diffuse loss of hair", "Oral or nasal ulcerations", "Pleuritic chest pain with pleural rub or effusion or pleural thickening", "Pericardial pain with at least 1 of the following: rub, effusion, or electrocardiogram or echocardiogram confirmation", "Decrease in CH50, C3, or C4 below the lower limit of normal for testing laboratory", "Increased DNA binding by Farr assay above normal range for testing laboratory", ">38° C. Exclude infectious cause", "<100,000 platelets/× 10^9/L, exclude drug causes", "<3000 white blood cells/× 10^9/L, exclude drug causes."])
SLEDAI_weight = np.array([8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1])
SLEDAI_ans = np.array(None, (object, [24]))
SLEDAI_ans_num = SLEDAI_ans.copy()
##-------------------------------------------------------------我是分隔線-----------------------------------------------------------------##
### 二、各流程與函數呼叫
# 在初始介面先使用二分法確認使用者狀態(類似分類樹概念)
import SLEfunc.SLE as SLEF
status1 = SLEF.Qstatus()
status3 = 'N'   #當classify as not SLE時，不會再問QbeforeDAI，因此預設為'N'

if status1 == 'N':   #進入classification
  #entry criterion
  titer = SLEF.entry_criterion()
  if titer <= 80:   
    # SLE additive criteria各condition問答 (利用巢狀while loop 處理與使用者的問答以及答題紀錄，適用於clinical & immunological) 
    SLE_ans = SLEF.ConditionCriteria_QA(SLE_domain, SLE_cond, SLE_ccond, SLE_ans, SLE_loop_control)
    #ans confirmation(分為clinical & immunological)##
    SLEF.Ans_Confirmation(SLE_cond, SLE_ans, SLE_loop_control)
    #Data-processing: SLE_ans 轉換為 ans_Number_array(-1, 0, 1)    
    SLE_ansNum, SLE_ansNI, SLE_ans_Weight = SLEF.Change_YN_to_Number(SLE_ans) 
    #找出各domain最高分
    Domain_weight, total_score = SLEF.Find_Domain_Max(SLE_ans_Weight)
    # 找到weight最高的domain  >>判定main determinant instead of major cause!!! 
    main_cdeterminant, main_ideterminant = SLEF.Find_Main_Detreminamt(Domain_weight, SLE_domain, SLE_ccond)
    # 最終結果與呈現診斷建議
    sleresult = SLEF.SLE_Classification_Advice(total_score, Domain_weight, SLE_ccond)
    # No_Information_Suggestion
    SLE_NI_Cond = SLEF.NI_Suggestion1(SLE_ansNI, SLE_domain, SLE_cond)
  else:
    sleresult = 'No'
    print('\nDiagnostic result:')
    print('This patient is probably not classified as SLE because he/she doesn\'t the entry criterion!')
  print("\nReference: The result is based on the 2019 EULAR/ACR classification criteria of SLE.")
  
  # 如果probably classified as SLE >>> 詢問使用者是否想進入SLEDAI了解嚴重度分級
  if sleresult.startswith('Yes'): #and titer <= 80可省略?!
    status3 = SLEF.QbeforeDAI()
  else:
    pass  
else:
  status3 = SLEF.QbeforeDAI()  
##-------------------------------------------------------------我是分隔線-----------------------------------------------------------------##
#如果使用者有意願 >>> 用SLEDAI進一步嚴重度分級  #盡量不要重複問(Fever, Thrombocytopenia, Psychosis, Seizure, Proteinuria)
if status3 == 'N':
  print('Thank you for using this App! Bye!')
else:
  # SLEDAI各condition問答 (先不做科別的分類)/ 問答時已產生SLEDAI_ans_num(0無症狀或無資料, 1有症狀)
  SLEDAI_ans, SLEDAI_ans_num = SLEF.SLEDAI_QA(SLEDAI_cond, SLEDAI_def)
  # SLEDAI_Ans_Confirmation
  SLEDAI_ans, SLEDAI_ans_num = SLEF.SLEDAI_Ans_Confirmation(SLEDAI_cond)
  #計算總分
  SLEDAI_TrueWeight, SLEDAI_total = SLEF.SLEDAI_Process()
  # SLEDAI分級與final suggestion
  SLEDAIClass = SLEF.SLEDAI_Class(SLEDAI_total)
  # No_Information_Suggestion
  SLEDAI_NI_Condition = SLEF.NI_Suggestion2(SLEDAI_ans, SLEDAI_cond)
  print(f'''\nRegerence: The result is based on SLEDAI-2K(30 Days).2010.  Thank you for your patronage!''')
SLEF.ExcelAuto()  #將病患資料自動記錄於Excel  