#!/usr/bin/env node
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const root = '/home/ubuntu/north-phase2c';
const context = { window: {}, Object, Array, String, Number, Boolean, console };
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root, 'assets/north-config.js'), 'utf8'), context);
const source = context.window.NORTH_CONFIG;
const tools = Object.fromEntries(Object.entries(source.products).filter(([, item]) => item.category === 'free-tools' && item.availability === 'available'));
const payload = {
  brand: { appStoreUrl: source.brand.appStoreUrl },
  publicWebLanguage: source.publicWebLanguage,
  products: tools,
  analytics: { allowedEvents: source.analytics.allowedEvents.filter((event) => ['library_view','free_tool_start','free_tool_complete','free_tool_recommendation','app_store_click'].includes(event)) }
};
fs.writeFileSync(path.join(root, 'assets/free-tools-config.js'), `(function (window) { 'use strict'; window.NORTH_CONFIG = Object.freeze(${JSON.stringify(payload, null, 2)}); })(window);\n`);
console.log(JSON.stringify({freeTools:Object.keys(tools).length, analytics:payload.analytics.allowedEvents.length}, null, 2));
