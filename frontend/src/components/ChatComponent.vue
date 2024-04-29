<!-- <template>
  <div class="chat">
    <div class="chat-messages" ref="chatMessages">
      <div v-for="(message, index) in messages" :key="index" class="message">
        {{ message }}
      </div>
    </div>
    <input
      v-model="newMessage"
      @keyup.enter="sendMessage"
      placeholder="Escribe un mensaje..."
    />
    <button @click="sendMessage">Enviar</button>
  </div>
</template> -->
<template>
  <div class="q-pa-md row justify-center">
    <div style="width: 100%; max-width: 400px">
      <q-chat-message
        label="Sunday, 19th"
      />

      <q-chat-message
        name="me"
        avatar="https://cdn.quasar.dev/img/avatar4.jpg"
        :text="['hey, how are you?']"
        sent
        stamp="7 minutes ago"
      />
      <q-chat-message
        name="Jane"
        avatar="https://cdn.quasar.dev/img/avatar3.jpg"
        :text="['doing fine, how r you?']"
        stamp="4 minutes ago"
      />
    </div>
  </div>
    <input
      v-model="newMessage"
      @keyup.enter="sendMessage"
      placeholder="Escribe un mensaje..."
    />
    <button @click="sendMessage">Enviar</button>
</template>

<script setup>
import { ref } from "vue";

const messages = ref([]);
const newMessage = ref("");

const sendMessage = () => {
  if (newMessage.value.trim() !== "") {
    messages.value.push(newMessage.value);
    newMessage.value = ""; // Limpiar el campo de entrada después de enviar el mensaje

    // Desplazarse automáticamente hacia abajo para mostrar el último mensaje
    const chatMessages = document.querySelector(".chat-messages");
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
};
</script>

<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  height: 400px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  border: 1px solid #ccc;
  padding: 10px;
}

.message {
  background-color: #f0f0f0;
  padding: 5px;
  margin-bottom: 5px;
}

input {
  margin-top: 10px;
  padding: 5px;
  font-size: 16px;
  border: 1px solid #ccc;
}

button {
  margin-top: 5px;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
}
</style>
