# ChatbotHistory_Langchain


Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak küçük çaplı chatbot projesi geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

Projede, Gemini AI ile birlikte Langchain framework'ü kullanılmıştır. Langchain, büyük dil modelleri ile uygulama geliştirilmesinde kullanılmaktadır. Output ve input değerlerini isteğimize göre filtrelenmesini, zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır.

Geliştirilen chatbot, hafızasında eski mesajları tutarak kullanıcıya tutarlı cevaplar vermektedir. Burada **__session id__** kullanılarak chat geçmişi tutulmaktadır. Aynı session id'de olunduğu sürece chat kısmına yazılan mesajlar tutulmaktadır / kaybolmamaktadır. Çalışmada çıktı üretirken __invoke__ fonksiyonu yerine __stream__ kullanılmıştır. Invoke, tüm çıktıyı aynı anda görmeyi sağlamaktadır. Stream ise çıktıyı kelime kelime parçalar şeklinde görmeyi sağlamaktadır. Kullanılacak amaca göre kullanımı ayarlanabilmektedir. Örnek bir çıktı Şekil 1'de görülmektedir.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/884e5085-d2ef-4724-a1dc-c13c56ddbfa4" alt="image">
</div>
Şekil 1. Geliştirilen chatbot'un verdiği cevaplara bir örnek

<br>
<br>

