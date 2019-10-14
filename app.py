<!DOCTYPE html>
<html>
  <title>Business Intelligence chatbot</title>
  
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <style>
      body {
        font-family: monospace;
      }
     
      h3 {
        color: black;
        font-size: 20px;
        margin-top: 3px;
        text-align: center;
      }
      #chatbox {
        margin-left: auto;
        margin-right: auto;
        width: 40%;
        margin-top: 60px;
      }
      #userInput {
        margin-left: auto;
        margin-right: auto;
        width: 40%;
        margin-top: 60px;
      }
      #textInput {
        width: 90%;
        border: none;
        border-bottom: 3px solid black;
        font-family: monospace;
        font-size: 17px;
      }
      .userText {
        color: white;
        font-family: monospace;
        font-size: 17px;
        text-align: right;
        line-height: 30px;
      }
      .userText span {
        background-color: #808080;
        padding: 10px;
        border-radius: 2px;
      }
      .botText {
        color: white;
        font-family: monospace;
        font-size: 17px;
        text-align: left;
        line-height: 30px;
      }
      .botText span {
        background-color: #4169e1;
        padding: 10px;
        border-radius: 2px;
      }
      #tidbit {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 300px;
      }
      .boxed {
        margin-left: auto;
        margin-right: auto;
        width: 78%;
        margin-top: 60px;
        border: 1px solid green;
      }
      .box {
        border: 2px solid black;
      }
    </style>
  </head>
  <body>
    <img />
    <center>
      <h1>
       Your Personal ChatBot
      </h1>
    </center>
   
    
    <div class="boxed">
      <div>
        <div id="chatbox">
          
          <p class="botText">
            <span>Hi! How May I help you?</span>
          </p>
        </div>
        <div id="userInput">
          <input id="textInput" type="text" name="msg" placeholder="Message" />
        </div>
      </div>
      <script>
        function getBotResponse() {
          var rawText = $("#textInput").val();
          var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
          $("#textInput").val("");
          $("#chatbox").append(userHtml);
          document
            .getElementById("userInput")
            .scrollIntoView({ block: "start", behavior: "smooth" });
          $.get("/get", { msg: rawText }).done(function(data) {
            var botHtml = '<p class="botText"><span>' + data + "</span></p>";
            $("#chatbox").append(botHtml);
            document
              .getElementById("userInput")
              .scrollIntoView({ block: "start", behavior: "smooth" });
          });
        }
        $("#textInput").keypress(function(e) {
          if (e.which == 13) {
            getBotResponse();
          }
        });
      </script>
    </div>
  </body>
</html>
