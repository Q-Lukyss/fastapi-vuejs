<template>
  <h1>Auteur</h1>

  <ul v-if="auteurs_list.length > 0">
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

axios.defaults.withCredentials = true;
// axios.defaults.headers.common['Origin'] = 'http://frontend:3000'; // Définition de l'origine correcte

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
      axios
        // .get('http://backend:8000/api/auteurs') marche pas
        .get('http://localhost:8200/api/auteurs') // fonctionne parfaitement
        .then(response => {
          this.auteurs_list = response.data
          // console.log('Succes ' + response.data)
        })
        .catch(error => {
          console.error('Erreur mounted', error)
        });
    },
    getRoot() {
      axios
        .get('http://localhost:8200/')
        .then(response => {
          console.table('Succes ' + response.data)
        })
        .catch(error => {
          console.error('Erreur mounted', error)
        });
    }
  },
}
</script>
