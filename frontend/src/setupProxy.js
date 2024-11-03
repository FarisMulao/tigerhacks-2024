const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/login",
    createProxyMiddleware({
      target: "http://localhost:5000/upload",
      changeOrigin: true,
    })
  );

  app.use(
    "/upload",
    createProxyMiddleware({
      target: "http://localhost:5000/upload",
      changeOrigin: true,
    })
  );
};
