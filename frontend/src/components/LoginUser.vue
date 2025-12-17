<template>
    <div>
        <h1>Login</h1>
        <input v-model="username" pkaceholder="Enter your username" />
        <input v-model="password" type="password" placeholder="Enter your password" />
        <button @click="login">Login</button>
    </div>
</template>
<script>
    import axios from "axios";

    export default {
        data() {
            return {
                username: "",
                password: ""
            };
        },
        methods: {
            async login() {
                try {
                    await axios.post("http://127.0.0.1:5000/login", {
                        username: this.username,
                        password: this.password
                    });
                    // this.$router.push("http://127.0.0.1:5000/dashboard");
                    alert("Login successful!");
                } catch {
                    alert("Login failed. Please check your credentials.");
                }
            }
        }
    };
</script>