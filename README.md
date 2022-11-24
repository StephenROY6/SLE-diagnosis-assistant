# 1113_SLE_Diagnosis_Assistant_
**新增功能:**
1. 執行時可一次輸入多個病人
2. 詢問是否儲存，再整合在excel
3. 紀錄每位病人當下時間

# 1010_SLE_Diagnosis_Assistant_integtrated
**整合結果：**\
1.輸入介面精簡\
2.ans confirm可一次修改多題\
3.病人資料的excel自動化\
4.打包package使主程式精簡至80行內，並能順利運行

# 0821__SLEClassification&SLEDAI_for_users(NEWEST)
**此版特點:**\
1.輔助說明內容的簡化、程式碼的精簡(變數名稱)\
2.當lupus nephritis選擇題輸入非規定的正整數時，雖然不會錯誤提醒，但也視同無效不會被計分；例外處理時，盡量讓電腦幫忙列出錯誤(eg.型態轉換不符)，其餘輸入型態正確但不合乎SLE臨床知識與邏輯等錯誤則盡量手動羅列。\
3. Ans_confirmation: 在處理資訊前提供目前答案給作答者參考，且呈現出容易判讀的dataframe格式，並能輸入題號做修正；修正完畢後再次提供目前作答情形給作答者參考，做資料處理與判讀前的最後確認(具有防呆裝置，限定輸入正確格式與題號)\
4. 文字前端與後端如果輸入時誤打空白建，則系統會自動刪除 (利用str.strip())

疑問:\
為何用python.exe執行到最後一步時，還來不及看到最終結果就馬上exit了??

# 0727_SLEClassification&SLEDAI_for_users(NEWEST)
**此版特點:**\
1.在初始介面先使用二分法確認使用者狀態(類似分類樹概念)\
2.問答方式合理化: Proteinuria > 0.5g/24hr 讓使用者填數字 ； Renal Biopsy為選擇題(Class II or lll or IV or V只會有一個)\
2.SLEDAI先不分類
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
  
# 0711_SLE_DiagnosisAssistant___ClassificationAndSLEDAI
(after 0704, 0711 meeting) contain Classification and SLEDAI；store ans, weight in 2-D nparray

***延續SLE_2-2特色:** \
1.防呆裝置：在問答時，titer若出現非正浮點數，則請使用者重填；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者在填一次(而非資料處理時請他重填)

2.將前置作業、問答過程與後續資訊處理與運算分開處理，方便於未來診斷標準更新時，只須修改前面的資料(weight_array、condition_array)即可。 

***此版新增特色:** \
1.運用*numpy array(2-D Array)做為資料儲存、資訊處理主軸(結構大改版，不同於以往的dict + nested list)，方便未來以矩陣執行更快速且多元的運算、能有更多資料分析(eg.統計學、ML)套件

2.增加問答過程中使用者可使用的功能(Y、N、None、B、F):使用者能跳至先前或後面的題目更改答案，如不想更改答案也可直接返回不須重新填答: 善用巢狀while loop，當輸入B(back)或F(forward)時，讓使用者知道自己正跳至別題檢查，並可更正答案，在每個domain填答完後自動呈現出目前答題情形；同時新增No information的項目，處理缺乏資訊的狀況，並在結果呈現時，讓使用者知道哪個domain_condition的檢測資訊遺漏(hint: 事先將其index儲存於變數ans_No_Information)。
  
3.更加注意2019 EULAR/ACR classification criteria of SLE 以及 SLEDAI-2K(30 Days).2010 文章中診斷指示的細節(eg.SLE classification requires at least one clinical criterion)，並實踐於此版程式中(eg.問答前詳細說明判定標準，了解後才可進入作答區；將分數最高的domain解讀為判定main determinant instead of main cause；
呈現判讀結果後利用No_Information_Suggestion函數告知使用者資訊遺漏的欄位，告知其隱含意義；程式碼最後提供reference)

4.將問答、資料處理的程序打包為function(以關鍵字命名)，使code呈現時更加簡潔明瞭，方便與共同開發者分享交流。(It seems that 個人使用numpy後發現其內建函數的用處，能減少資訊處理時自訂函數的麻煩)

***未來展望:**

1.目前在每個domain填答完後會自動呈現出目前答題情形，但其結構為2-D array，較占版面、對使用者而言可讀性較低；希望後續能改善為「作答時呈現出該題目的目前答案給使用者參考」

2.2019 EULAR/ACR classification criteria of SLE 以及 SLEDAI-2K(30 Days).2010的症狀中只有約5項相同，且此兩份問卷的時間設定*似乎不太一樣(classification criteria of SLE只要出現過一次即可；而SLEDAI的評分標準是過去三十天內是否曾經出現某個症狀)；另外，這兩個程序個別的症狀判定標準不太一樣(即使名稱相同)。因此，個人決定全部重新問答一次，此部分作法是否恰當或有更好的執行方式待與老師、同學討論後修正。

3.不確定目前的2-D array是否就是matrix，或可簡單地做轉換，希望對numpy matrix操作更熟悉後再做修正  
  
# 0628_SLE_diagnosis_assistant_2
after 0627 meeting

目前產出三版:\
**使用者版2-2精進之處:(142 lines)**\
(1)在問答時，titer若出現非正浮點數，則請使用者重填；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者再填一次(而非資料處理時請他重填) (2)更加善用dict的"參照"功能(注意：dict用於標籤簡單、特定關鍵字時) WAY1:同樣先彙整問答時的資料，再做後續的答案與分數轉換 (3)試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。

**使用者版2-3精進之處:(126 lines)**\
(1)在問答時，titer若出現非正小數，則請使用者重填；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者再填一次(而非資料處理時請他重填) (2)更加善用dict的"參照"功能(注意：dict用於標籤簡單、特定關鍵字時) WAY2:問答時直接判斷、參照並產生trueweight (3)試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。

**使用者版2-4精進之處: (最為精簡: 120 lines)**\
(1)在問答時，titer若出現非正小數，則請使用者重填?!；condition問答時若出現非Y或N的字元，將回到loop上個問題，讓填入者再填一次(而非資料處理時請他重填) (2)預先填入陽性時的分數，問答時直接判斷並產生trueweight(如陰性則改為0)，較無用到字典參照 (3)試著將前置作業(dict維護)與後續資訊處理與運算分為兩部分，方便於未來診斷標準更新時，只須修改前面的dict即可。(本次盡量將後面各變數參照至一個(或少數個)來源資料，減少診斷標準改變時可能出現版本維護不易之問題) (4)各執行階段之間間隔一行、更加格式化

**此三版的比較如下**:
(1)2-2為先彙整問答時的資料，再做後續的答案(Ans)與分數(trueweight)轉換；2-3、2-4則在問答時直接判斷使用者輸入的答案，進一步判斷並產生trueweight，少了容納答案的list變數: Ans_clinical & Ans_immunological，以及簡化「輸入資訊處理產生結果」的過程: 不須答案(Ans)與分數(trueweight)轉換，也因此codes較為精簡。
/個人認為：　當輸入資料的型態單純、判斷方式簡單時，可在迴圈中邊輸入邊判斷，直接產生即將用來判斷的分數表；然而，當輸入資料的型態複雜、需要繁雜運算時，則宜將答案蒐集以及資料處理清楚分隔，先蒐集答案，再進行資訊轉換和處理，避免使用者耗費大量時間等待系統運算，導致使用者輸入效率減低或對系統產生壞印象。
/此外，將答案蒐集以及資料處理清楚分隔也有助於版本維護或系統出現錯誤時，清楚地得知哪個區塊出現bug。
(2)2-3、2-4的差異為: 2-3在問答時直接判斷、參照並產生trueweight；而2-4則預先在trueweight填入陽性時的分數，問答時可視情形修改(如陰性則改為0)、直接產生病患各症狀所得分數表，較無用到字典參照。
/個人認為:　在分類較簡單的系統中(eg.症狀只有Y、N二分法)，無須特別運用字典參照，利用預先建立的陽性分數表，碰到陰性時再改為0反而容易許多； 當狀況較複雜時，使用預先設定的字典進行參照 則可能 比建立多個分數表方便。
