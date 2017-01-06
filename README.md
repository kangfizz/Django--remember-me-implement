# Django--remember-me-implement
###This topic is talking about how to implement "remember me" checkbox  
**中文說明:參考views.py 跟 html檔案**  
```
1.基本上是利用request.session['變數名']  來做 def之間的傳遞  
2.不需要經過url  
3.在url也可以設定{{request.session.變數名}} 來取得改變過後的值(尤其是換頁)  
4.同樣可以利用在查詢選項時,換頁後能固定你剛剛選擇之變數的方法。
```
