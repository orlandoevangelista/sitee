import flask

app = flask.Flask(__name__)

@app.route('/home')
def home():
    
    html = """
    <html>
    <head><title>project</title></head>
    <body>
    
    <style>
    body {
        margin:0;
    }
    #menu{
        position: absolute;
        background: black;
        height: 400px;
        width:200px;
        left: -200px;
    }
    div.oi{
        background: red;
        height:50px;
        width: 50px;
    }
    #nn {
    color: white;
    font-size: 20px;
    text-align: center;
    
    }
    
    </style>
    
    <h1 id="test"></h1>
    <div class="oi" onmouseover="go()" onclick="out()"></div>
    <div id="menu">
    <div id="nn" >MENU</div>
    
    </div>


        
    <script>
    var num = -200;
    function go(){
        var tatu = setInterval(function la(){
            num += 1;
            document.getElementById("menu").style.left=num;
            if (num > 1){
                clearInterval(tatu);

            }

        },1)

    }
    function out(){
        var ara = setInterval(function lo(){
            num -= 1;
            document.getElementById("menu").style.left=num;
            if (num < -200){
                clearInterval(ara);

            }

        },1)

    }




    
    </script>
    </body>
    </html>
    
    """
    return html

if __name__ == "__main__":
    app.run(port=5555)
