<template>
  <v-card elevation="2">
    <v-card-title>
      <v-icon class="mr-4" large>mdi-kubernetes</v-icon>
      Kubernetes info
    </v-card-title>
    <v-card-subtitle>
      Information about the Kubernetes cluster running this container.
    </v-card-subtitle>
    <v-card-text class="mt-2">
      <h4 class="font-weight-regular">backend-api pod status: {{ backend_status }}</h4>
      <h4 class="font-weight-regular">pod that served this response: {{ backend_podname }}</h4>
    </v-card-text>
    <v-card-actions>
      <v-btn color="blue darken-1" text @click="getKubernetesInfo">
        Get Info
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      backend_status: '',
      backend_podname: '',
    }
  },
  methods: {
    getKubernetesInfo() {
      this.$axios.get('http://api.k8s.aguest.me/healthcheck').then((response) => {
        this.backend_status = response.data.status;
        this.backend_podname = response.data.hostname;
      })
    }
  }
}
</script>