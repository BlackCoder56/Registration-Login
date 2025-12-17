<template>
    <div>
        <h2>Register</h2>
        <input v-model="username" placeholder="Enter your username" />
        <input v-model="password" type="password" placeholder="Enter your password" />
        <button @click="register">Register</button>
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
            async register() {
                await axios.post("http://127.0.0.1:5000/register", {
                    username: this.username,
                    password: this.password
                });
                alert("Registration successful!");
            }
        }
    }
</script>