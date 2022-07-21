# 0621_SLE-diagnosis-assistant
(一)目的：提供一個方便醫護人員(不限醫師，可以是專科護理師、甚至實習護理師)操作的程式碼，幫助建立使用者友善的系統性紅斑性狼瘡人機互動平台。\
(二)目前成果與功能：\
  1.前置作業pre-dataprocessing：establish several dicts as reference table for various conditions in each domain
  2.問答介面：(1)依照domain分門別類，先呈現特定domain名稱讓填寫者明瞭，再依序提問該domain的子題讓填寫者輸入。
             (2)並將輸入結果分門別類放置於nested list中，方便後續一對一地轉換為分數以及結果分析。
  3.資訊處理與計算結果：
    (1)利用先前放至於Nested list中分類好的答案，將if 判斷式放置於for loop中，依序呈現出對應的weight，放置於框架相同的Nested list中。
    (2)將Nested list中的元素(特定domain的weight_list)整合為單一數值(利用max()，輸出domain最大值)，成為一個list。
    (3)資料處理時，如果先前填寫者誤填Y、N以外的字元，則無法成功轉換為分數、比較最大值，將出現error以及警示標語，必須重填!!!
    (3)可呈現最後total_weight並判斷是否為SLE；若是SLE，則呈現出占分最高的domain，最為醫師後續療程的參考。
(三)下一版將精進之處    
  1.在問答時，若出現非Y或N的字元，將回到loop上個問題，讓填入者在填一次(而非資料處理時請他重填)
  2.更加善用dict的"參照"功能/注意：dict用於標籤簡單、特定關鍵字時
  3.試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。
(四)未來展望
  1.differential diagnosis
  2.concise codes
  3.介面優化、盡量簡單明瞭；後端處理仍需精簡、但相較前者，可稍微複雜
  4.將技術端(我們) 與 醫護需求端 整合，成功做出SLE人機互動平台。
  
  
# 0628_SLE_diagnosis_assistant_2
after 0627 meeting
目前產出三版:
使用者版2-2精進之處:(142 lines)
(1)在問答時，titer若出現非正浮點數，則請使用者重填；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者再填一次(而非資料處理時請他重填) (2)更加善用dict的"參照"功能(注意：dict用於標籤簡單、特定關鍵字時) WAY1:同樣先彙整問答時的資料，再做後續的答案與分數轉換 (3)試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。

使用者版2-3精進之處:(126 lines)
(1)在問答時，titer若出現非正小數，則請使用者重填；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者再填一次(而非資料處理時請他重填) (2)更加善用dict的"參照"功能(注意：dict用於標籤簡單、特定關鍵字時) WAY2:問答時直接判斷、參照並產生trueweight (3)試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。

使用者版2-4精進之處: (最為精簡: 120 lines)
(1)在問答時，titer若出現非正小數，則請使用者重填?!；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者再填一次(而非資料處理時請他重填) (2)預先填入陽性時的分數，問答時直接判斷並產生trueweight(如陰性則改為0)，較無用到字典參照 (3)試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。(本次盡量將後面各變數參照至一個(或少數個)來源資料，減少診斷標準改變時可能出現版本維護不易之問題) (4)各執行階段之間間隔一行、更加格式化

此三版的比較如下:
(1)2-2為先彙整問答時的資料，再做後續的答案(Ans)與分數(trueweight)轉換；2-3、2-4則在問答時直接判斷使用者輸入的答案，進一步判斷並產生trueweight，少了容納答案的list變數: Ans_clinical & Ans_immunological，以及簡化「輸入資訊處理產生結果」的過程: 不須答案(Ans)與分數(trueweight)轉換，也因此codes較為精簡。
/個人認為：　當輸入資料的型態單純、判斷方式簡單時，可在迴圈中邊輸入邊判斷，直接產生即將用來判斷的分數表；然而，當輸入資料的型態複雜、需要繁雜運算時，則宜將答案蒐集以及資料處理清楚分隔，先蒐集答案，再進行資訊轉換和處理，避免使用者耗費大量時間等待系統運算，導致使用者輸入效率減低或對系統產生壞印象。
/此外，將答案蒐集以及資料處理清楚分隔也有助於版本維護或系統出現錯誤時，清楚地得知哪個區塊出現bug。
(2)2-3、2-4的差異為: 2-3在問答時直接判斷、參照並產生trueweight；而2-4則預先在trueweight填入陽性時的分數，問答時可視情形修改(如陰性則改為0)、直接產生病患各症狀所得分數表，較無用到字典參照。
/個人認為:　在分類較簡單的系統中(eg.症狀只有Y、N二分法)，無須特別運用字典參照，利用預先建立的陽性分數表，碰到陰性時再改為0反而容易許多； 當狀況較複雜時，使用預先設定的字典進行參照 則可能 比建立多個分數表方便。
