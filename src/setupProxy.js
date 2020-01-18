const proxy = require("http-proxy-middleware");

module.exports = function(app) {
  app.use( 
    "/api/org/*",  
    proxy({ 
      target: "http://localhost:8000/", 
      changeOrigin: true
    })
  );
  app.use(
    "/api/rest-auth/login/",
    proxy({
      target: "http://localhost:8000/"
    })
  );
};