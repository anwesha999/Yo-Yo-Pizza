<template>
  <div id="app">
    <chatComponentVue/>
  </div>
</template>

<script>
// import Chat from './components/Chat'
import chatComponentVue from './components/chatComponent.vue'

export default {
  name: 'App',
  components: {
    chatComponentVue
  }
}
</script>

<style>

</style>
