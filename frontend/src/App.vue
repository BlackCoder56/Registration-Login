<template>
  <RegisterUser />
  <LoginUser />
</template>

<script>
import RegisterUser from './components/RegisterUser.vue';
import LoginUser from './components/LoginUser.vue';

export default {
  name: 'App',
  components: {
    RegisterUser,
    LoginUser
  }
}
</script>

<style scoped>
</style>
