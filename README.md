# SLE-diagnosis-assistant
(一)目的：提供一個方便醫護人員(不限醫師，可以是專科護理師、甚至實習護理師)操作的程式碼，幫助建立使用者友善的系統性紅斑性狼瘡人機互動平台。
(二)目前成果與功能：
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
