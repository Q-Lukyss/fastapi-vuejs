<template>
  <h1>Auteur</h1>

  <ul v-if="auteurs_list != null">
    Listes des auteurs
    <li v-for="auteur in auteurs_list">
      {{ auteur.nom }}
      {{ auteur.prenom }}
    </li>
  </ul>

  <p v-else>Pas d'auteurs dans la bibliothèque</p>
</template>

<script>
import axios from "axios";

export default {
  components: {
  },
  data() {
    return {
      auteurs_list: [],
    }
  },

  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      axios.get('http://backend:8000/api/auteurs')
          .then(response => {
            this.auteurs_list = response.data
          })
          .catch(error => {
            console.error('Erreur mounted', error)
          });
    },
  },
}
</script>
