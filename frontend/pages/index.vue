<template>
  <v-row  align="center" class="mt-2">
    <v-col cols="8" sm="8" md="6">
      <dog-facts />
    </v-col>
    <v-col offset="1" cols="5" sm="5" md="5">
      <kubernetes-info />
    </v-col>
  </v-row>
</template>

<script>
import DogFacts from '~/components/DogFacts.vue';
import KubernetesInfo from '~/components/KubernetesInfo.vue';


export default {
  components: { DogFacts, KubernetesInfo },
  
}
</script>
