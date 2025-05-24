# Django 後端系列文

本系列文章紀錄 Django 的實作過程，簡單的建立常用的數據 — 氣象資料作為介紹的主角。從簡單的資料串接開始，逐步導入資料庫設計與背景排程機制，讓天氣資料能夠持續自動累積。此設計旨在為未來報表呈現提供穩定且可用的數據基礎。

---

## 📘 系列文章

### 1️⃣ 我獨自 Django：開始我的 Django 專案  
👉 [Medium 文章連結](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E9%96%8B%E5%A7%8B%E6%88%91%E7%9A%84-django-%E5%B0%88%E6%A1%88-83d98bd32d94)

作為系列起點，本篇介紹：

- 專案規劃與開發環境準備  
- Django 專案與 app 架構建立  

---

### 2️⃣ 我獨自 Django：快速打造天氣 API 服務（上篇）  
👉 [Medium 文章連結](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E5%BB%BA%E7%AB%8B%E7%AC%AC%E4%B8%80%E5%80%8B-app-%E9%96%8B%E5%95%9F-api-%E5%AF%A6%E4%BD%9C%E4%B8%96%E7%95%8C-621a23e72eb0)

Django 後端開發，開始實作 API：

- Django Model 架構設計  
- 串接開源天氣 API  
- 初步建立 RESTful API（使用 Django REST framework）

---

### 3️⃣ 我獨自 Django：快速打造天氣 API 服務（中篇）  
👉 [Medium 文章連結](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E5%BF%AB%E9%80%9F%E6%89%93%E9%80%A0%E5%A4%A9%E6%B0%A3-api-%E6%9C%8D%E5%8B%99-%E4%B8%AD%E7%AF%87-f6890fd46866)

延續上一篇接著介紹 API 的應用：

- 儲存 API 回傳資料進資料庫  
- 建立序列化器（Serializers）與資料驗證  
- 說明多層級資料結構與 JSON 處理

---

### 4️⃣ 我獨自 Django：快速打造天氣 API 服務（下篇）  
👉 [Medium 文章連結](https://medium.com/@Alan620/%E6%88%91%E7%8D%A8%E8%87%AA-django-%E5%BF%AB%E9%80%9F%E6%89%93%E9%80%A0%E5%A4%A9%E6%B0%A3-api-%E6%9C%8D%E5%8B%99-%E4%B8%8B%E7%AF%87-257b6292f4d4)

使用排程利用 API 每日累積資料：

- 使用 Celery 實作每日天氣資料自動匯入  
- 整合 Redis 作為背景任務佇列  
- Django API 架構設計與擴展實踐  

---

## 📝 授權 License

本專案內容與程式碼遵循 [MIT License](./LICENSE)。

---

## 🙌 支持與關注

如果你覺得這個系列對你有幫助，歡迎幫我按下 Medium 上的 👏，或分享給更多對 Django 感興趣的朋友。

👉 [追蹤我的 Medium](https://medium.com/@Alan620)
