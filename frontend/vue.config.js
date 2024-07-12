const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: '../connect4/static/frontend',
  assetsDir: 'assets',
  indexPath: '../../templates/frontend/index.html',
  devServer: {
    proxy: 'http://localhost:8000',
  },
})
