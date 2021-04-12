const express =require("express");
const https =require('https');
const bodyParser = require("body-parser");

const app=express();

app.use(bodyParser.urlencoded({extended:true}));

app.get("/",function(req,res){
res.sendFile(__dirname +"/index.html");
app.use(express.static("public"));

});

app.post("/",function(req,res){


query=req.body.name;
const url="https://newwordsapi.herokuapp.com/countries/"+query;
https.get(url , function(response){
   console.log(response.statusCode);



response.on("data",function(data){
 const wordsData= JSON.parse(data);

 const words =wordsData.words;
 res.write("<h1>The new English words in the last decade from the country "+ query+" are"+ words+".</h1> ");

res.send();

});
});

 });


app.listen(process.env.PORT || 3000  , function(){
  console.log("Server is running on port 3000")
});