const bodyParser= require("body-parser");
const ejs =require("ejs");
const mongoose =require("mongoose");
const express =require("express");

const app =express();

app.set("view engine",'ejs');

app.use(bodyParser.urlencoded({extended:true}));

app.use(express.static("public"));

mongoose.connect("mongodb+srv://admin-Ishita:ishitagmongo1968@cluster0.3oovf.mongodb.net/PopularEnglishWordsDB",{useNewUrlParser:true});
const wordSchema = new mongoose.Schema({
  Country : String,
    word_1 : String,
    word_2 : String,
    word_3 : String,
    word_4 : String,
    word_5 : String,
    word_6 : String,
    word_7 : String,
    word_8 : String,
    word_9 : String,
    word_10 : String,
});
const word = mongoose.model("word",wordSchema);


app.get("/",function(req,res){
  res.sendFile(__dirname,"index.html")

  word.find({},function(err,foundwords){
    if(!err){
      res.send(foundwords)

    }else{
      console.log(err);
    }
});
});

app.listen( process.env.PORT || 3000 ,function(){
  console.log("server is up and running on port 3000");
});