from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Özür Dilerim</title>

<style>
body{
    margin:0;
    background:#050505;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    color:white;
    overflow:hidden;
    font-family:Arial;
}

.container{
    display:flex;
    gap:40px;
    align-items:center;
}

.card{
    width:280px;
    height:420px;
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 0 25px rgba(255,255,255,0.2);
}

.card img{
    width:100%;
    height:100%;
    object-fit:cover;
}

.center{
    text-align:center;
}

h1{
    font-size:60px;
    text-shadow:0 0 20px #ff0055;
}

button{
    padding:18px 40px;
    border:none;
    border-radius:50px;
    background:#ff0055;
    color:white;
    font-size:20px;
    cursor:pointer;
}

.floating-heart{
    position:absolute;
    color:pink;
    animation:float 6s linear infinite;
}

@keyframes float{
    from{transform:translateY(100vh);}
    to{transform:translateY(-10vh);}
}
</style>
</head>

<body>

<div class="container">

    <div class="card">
        <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1">
    </div>

    <div class="center">
        <h1>Özür Dilerim</h1>
        <p>Sana söz veriyorum, bir daha olmaz.</p>
        <button onclick="alert('❤️ Barışalım mı?')">Barışalım mı?</button>
    </div>

    <div class="card">
        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e">
    </div>

</div>

<script>
for(let i=0;i<25;i++){
    let h=document.createElement("div");
    h.className="floating-heart";
    h.innerHTML="❤️";
    h.style.left=Math.random()*100+"vw";
    h.style.fontSize=(20+Math.random()*30)+"px";
    h.style.animationDuration=(3+Math.random()*5)+"s";
    document.body.appendChild(h);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
