var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var session = require('express-session');
var RedisStore = require('connect-redis')(session);
var http = require('http');
var socket = require('socket.io');

var indexRouter = require('./routes/index');
var ajustesRouter = require('./routes/ajustes');

var app = express();

var http = http.Server(app);
var io = socket(http);

io.on('connection',(socket)=>{
    console.log('Novo usuario');
});
var solicitacoesRouter = require('./routes/solicitacoes')(io);
var delegacoesRouter = require('./routes/delegacoes')(io);
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(session({
  // store: new RedisStore({
  //   host: 'localhost',
  //   port:63791
  // }),
  secret: 'p@ssw0rd1',
  resave: true,
  saveUninitialized:true
}))

app.use(function(req,res,next){
  urls = ['/login','/','/contato', '/sobre'];
  if(urls.indexOf(req.url) === -1 && !req.session.usuario){
    res.redirect("/login");
  }else if(urls.indexOf(req.url) != -1 && req.session.usuario!=null){
    res.redirect("/inicio");
  }else{
    next();
  }
});
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/solicitacoes', solicitacoesRouter);
app.use('/delegacoes', delegacoesRouter);
app.use('/ajustes', ajustesRouter);
// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

http.listen(3000,()=>{
  console.log('executando...');
});

// module.exports = app;
