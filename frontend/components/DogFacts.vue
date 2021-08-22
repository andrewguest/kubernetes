<template>
  <v-card elevation="2">
    <v-card-title>
      <v-icon class="mr-4" large>mdi-dog</v-icon>
      Dog facts
    </v-card-title>
    <v-card-subtitle>
      This is an example of a Kubernetes deployment (this frontend) connecting to and retrieving information from another deployment (the backend).
    </v-card-subtitle>
    <v-card-text class="mt-2">
      <ul v-for="(fact, i) in facts" :key="i">
        <li>{{ fact }}</li>
      </ul>
    </v-card-text>
    <v-card-actions>
      <v-btn color="blue darken-1" text @click="getDogFacts">
        Fetch Facts
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      facts: [],
    }
  },
  methods: {
    getDogFacts() {
      this.$axios.get('http://api.k8s.aguest.me/dogfacts').then((response) => {
        return this.facts = response.data["Dog facts"];
      })
    },
  }
}
</script>