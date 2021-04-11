const bodyParser= require("body-parser");
const ejs =require("ejs");
const mongoose =require("mongoose");
const express =require("express");


const app =express();

app.set("view engine",'ejs');

app.use(bodyParser.urlencoded({extended:true}));

app.use(express.static("public"));
mongoose.connect("mongodb+srv://admin-Ishita:ishita1968@cluster0.3oovf.mongodb.net/wordsDB",{useNewUrlParser:true});
const wordSchema = new mongoose.Schema({
  country : String,
    words : String,

});
const Country = mongoose.model("Country",wordSchema);


app.get("/",function(req,res){
  res.sendFile(__dirname,"/index.html")
});
app.get("/countries",function(req,res){
  Country.find({},function(err,foundwords){
    if(!err){
      res.send(foundwords)

    }else{
      console.log(err);
    }
});
});

app.get("/countries/:name",function(req,res){



  Country.findOne({country: req.params.name},function(err,result){
    if(result){
      res.send(result);

    }else{
      res.send("no words");

    }
  });
});


app.listen( process.env.PORT || 3000 ,function(){
  console.log("server is up and running on port 3000");
});