<template>
  <div>
    <table>
      <TableHead :columns="columns" />
      <TableBody>
        <TableRow v-for="item in data" :key="item.id">
          <TableData v-for="column in columns" :key="column" :value="item[column]" />
        </TableRow>
      </TableBody>
    </table>
    <button @click="adicionarRegistro">Adicionar Registro</button>
  </div>
</template>

<script>
import TableHead from './TableHead.vue';
import TableBody from './TableBody.vue';
import TableRow from './TableRow.vue';
import TableData from './TableData.vue';
import axios from 'axios';

export default {
  components: {
    TableHead,
    TableBody,
    TableRow,
    TableData,
  },

  data() {
    return {
      columns: ['id', 'codigo_acao', 'descricao', 'data', 'open', 'close', 'high', 'low', 'volume'],
      data: [
        {
          "id": 3,
          "codigo_acao": "ABC6.SA",
          "descricao": "Test admin Cassia",
          "data": "2023-06-20",
          "open": "50.00",
          "close": "50.00",
          "high": "50.00",
          "low": "50.00",
          "volume": 15
      
        },
        {
          "id": 1,
          "codigo_acao": "PTR4.SA",
          "descricao": "Test admin Cassia 8",
          "data": "2023-06-28",
          "open": "15.00",
          "close": "15.00",
          "high": "15.00",
          "low": "15.00",
          "volume": 5
        }
      ]
    };
  },

  mounted() {
    this.obterDadosTabela();
  },
  methods: {
    obterDadosTabela() {
      axios.get('http://localhost:8000/api/v1/acoes')
        .then(response => {
          this.data = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },

    adicionarRegistro() {
      const novoRegistro = {
        // Preencha com os dados do novo registro a ser adicionado
      };

      axios.post('http://localhost:8000/api/v1/acoes', novoRegistro)
        .then(() => {
          this.obterDadosTabela();
        })
        .catch(error => {
          console.error(error);
        });
    },

    editarRegistro(registro) {
      const registroAtualizado = {
        // Preencha com os dados atualizados do registro
      };

      axios.put(`http://localhost:8000/api/v1/acoes/${registro.id}`, registroAtualizado)
        .then(() => {
          this.obterDadosTabela();
        })
        .catch(error => {
          console.error(error);
        });
    },

    excluirRegistro(registro) {
      axios.delete(`http://localhost:8000/api/v1/acoes/${registro.id}`)
        .then(() => {
          this.obterDadosTabela();
        })
        .catch(error => {
          console.error(error);
        });
    },
  }
};
</script>
