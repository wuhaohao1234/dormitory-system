<template>
  <div>
    <div class="mb-2" >
      <el-button type="primary" @click="handleArrangement" >排列宿舍</el-button>
    </div>
  <el-table :data="users" style="width: 100%">
    <el-table-column prop="id" label="ID" width="50"></el-table-column>
    <el-table-column prop="account" label="学号"></el-table-column>
    <el-table-column prop="username" label="姓名"></el-table-column>
    <el-table-column label="宿舍号">
      <template #default="scope">
        <el-tag size="small">{{ scope.row.dormitory? scope.row.dormitory.dormitory : '暂无分配' }}</el-tag>
      </template>
    </el-table-column>
    <el-table-column label="详情">
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
          >编辑</el-button
        >
        <el-button
          size="small"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >删除</el-button
        >
      </template>
    </el-table-column>
  </el-table>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue';
import { ElMessage } from 'element-plus';
import 'element-plus/dist/index.css';
import { useUserStoreHook } from "@/store/modules/user";
// 模拟用户数据
const users = ref([]);

const handleDelete = () => {

}

const handleEdit = () => {

}

const handleArrangement = () => {

}

// 组件挂载时获取用户数据
onMounted(() => {
  useUserStoreHook().getUserList().then(res => {
    users.value = res.data.data;
  })
//   fetchUsers();
});
</script>

<style>
/* 你的样式可以放在这里 */
</style>
