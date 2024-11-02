import type { CapacitorConfig } from '@capacitor/cli';

/*const config: CapacitorConfig = {
  appId: 'com.plid.app',
  appName: 'plid',
  webDir: 'build'
};*/

const config: CapacitorConfig = {
  appId: 'com.plid.app',
  appName: 'plid',
  webDir: 'build',
  bundledWebRuntime: false, 
  android: {
    backgroundColor: '#FFFFFF', //  background color for splash screen on android
  },
  ios: {
    contentInset: 'automatic', // adjusts web view content inset on ios
  }
};


export default config;
