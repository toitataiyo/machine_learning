# 第5章 顧客の退会の予測
目的 : 前章ではクラスタリングにより行動パターンを分析した。行動パターンを分析できるということは、どのような顧客が退会するのかある程度予測可能。今回は決定木アルゴリズムによって顧客が退会するかどうか予測する  
想定 : 前回の詳細分析でいろんなことがわかった。ここまで分析してきたが、顧客を定着させ、増やすことを考えると、そもそも退会する人を防ぐ必要がある。どんな人が退会してしまうのか原因を知ることは可能?  

想定データ  
基本的に第3, 4章のデータと同じ  
・ジムの利用履歴 (logID, 顧客ID, 利用日)2018/4~2019/3    
・2019/3月末時点での会員データ (顧客ID, 名前, 会員クラス, 性別, 登録日, 退会日, キャンペーンID, 退会したかどうか)  
・会員区分データ (会員クラス, クラス名, 値段)  
・キャンペーン区分データ  (キャンペーンID, キャンペーン名称)
・第3章で作成した、利用履歴を含んだ顧客データ  
・第4章で作成した、利用履歴を年月/顧客毎に集計したデータ 