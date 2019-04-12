console.log(phantom.args);   // 被system模块的args替代, 现在是0
console.log(phantom.cookiesEnabled);
console.log(phantom.cookies);
console.log(phantom.libraryPath);
console.log(phantom.scriptName);
console.log(phantom.version['major'], phantom.version['minor'], phantom.version['patch']);

phantom.exit();