# 📚 系列技術文章目錄：Django x React

本系列文章紀錄以 Django + React 為基礎的全端實作流程。  
從後端 API 設計、資料排程、資料庫設計，到前端圖表呈現，逐步打造氣象資料可視化應用。  

---

## 🔧 Django 後端系列文

以氣象資料為主題，從 API 串接、資料儲存、到背景排程，建立穩定的數據服務。

### 1️⃣ 我獨自 Django：開始我的 Django 專案  
👉 [閱讀文章](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E9%96%8B%E5%A7%8B%E6%88%91%E7%9A%84-django-%E5%B0%88%E6%A1%88-83d98bd32d94)  
內容摘要：
- 專案規劃與開發環境準備  
- Django 專案與 app 架構建立  

### 2️⃣ 我獨自 Django：快速打造天氣 API 服務（上篇）  
👉 [閱讀文章](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E5%BB%BA%E7%AB%8B%E7%AC%AC%E4%B8%80%E5%80%8B-app-%E9%96%8B%E5%95%9F-api-%E5%AF%A6%E4%BD%9C%E4%B8%96%E7%95%8C-621a23e72eb0)  
內容摘要：
- Django Model 設計  
- 串接開源天氣 API  
- 初步建立 RESTful API（使用 DRF）

### 3️⃣ 我獨自 Django：快速打造天氣 API 服務（中篇）  
👉 [閱讀文章](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E5%BF%AB%E9%80%9F%E6%89%93%E9%80%A0%E5%A4%A9%E6%B0%A3-api-%E6%9C%8D%E5%8B%99-%E4%B8%AD%E7%AF%87-f6890fd46866)  
內容摘要：
- 將 API 資料儲存進資料庫  
- 建立序列化器與資料驗證  
- 處理 JSON 結構

### 4️⃣ 我獨自 Django：快速打造天氣 API 服務（下篇）  
👉 [閱讀文章](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E5%BF%AB%E9%80%9F%E6%89%93%E9%80%A0%E5%A4%A9%E6%B0%A3-api-%E6%9C%8D%E5%8B%99-%E4%B8%8B%E7%AF%87-257b6292f4d4)  
內容摘要：
- 使用 Celery + Redis 實作背景排程  
- 定時匯入每日天氣資料
- Django API 架構設計與擴展實踐

---

## ⚛️ React 前端系列文

React 前端串接 Django API，實現資料視覺化。

### 1️⃣ React 新手實戰：開始我的 React 專案  
👉 [閱讀文章](https://medium.com/@Alan620/react-%E6%96%B0%E6%89%8B%E5%AF%A6%E6%88%B0-%E9%96%8B%E5%A7%8B%E6%88%91%E7%9A%84-react-%E5%B0%88%E6%A1%88-17fd3761cd7f)  
內容摘要：
- React 簡介  
- 建立初始 React 專案 
- 專案目錄結構說明與核心概念介紹  

### 2️⃣ React 新手實戰：用天氣資料畫出趨勢圖（上篇）  
👉 [閱讀文章](https://medium.com/@Alan620/react-%E6%96%B0%E6%89%8B%E5%AF%A6%E6%88%B0-%E7%94%A8%E5%A4%A9%E6%B0%A3%E8%B3%87%E6%96%99%E7%95%AB%E5%87%BA%E8%B6%A8%E5%8B%A2%E5%9C%96-%E4%B8%8A%E7%AF%87-3b3eed81abd0)  
內容摘要：
- 串接 Django 提供的後端 API  
- 處理資料轉換與格式整理  

### 3️⃣ React 新手實戰：用天氣資料畫出趨勢圖（下篇）  
👉 [閱讀文章](https://medium.com/@Alan620/react-%E6%96%B0%E6%89%8B%E5%AF%A6%E6%88%B0-%E7%94%A8%E5%A4%A9%E6%B0%A3%E8%B3%87%E6%96%99%E7%95%AB%E5%87%BA%E8%B6%A8%E5%8B%A2%E5%9C%96-%E4%B8%8B%E7%AF%87-4f6c84d810a3)  
內容摘要：
- 模組化拆分 components、pages、services 架構
- 完整串接前後端，完成趨勢圖網頁

---

## 📝 授權 License

本專案內容與程式碼遵循 [MIT License](./LICENSE)。

---

## 🙌 支持與關注

如果你覺得這個系列對你有幫助，歡迎幫我按下 Medium 上的 👏，或分享給更多對 Django x React 感興趣的朋友。

👉 [追蹤我的 Medium](https://medium.com/@Alan620)
