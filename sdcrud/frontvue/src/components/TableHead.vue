<template>
  <thead>
    <tr>
      <th v-for="column in columns" :key="column">{{ column }}</th>
    </tr>
  </thead>
</template>

<script>
export default {
  props: ['columns']
};
</script>


