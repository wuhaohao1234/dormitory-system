<template>
    <div>
        <h2>个人信息</h2>
        <el-form ref="profileForm" :model="profileForm" label-width="120px">
            <el-form-item label="性别">
                <el-radio-group v-model="profileForm.gender">
                    <el-radio :value="1">男</el-radio>
                    <el-radio :value="2">女</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="家乡所在地区">
                <el-select v-model="profileForm.region" placeholder="请选择">
                    <el-option label="南方" value="south"></el-option>
                    <el-option label="北方" value="north"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="星座">
                <el-input v-model="profileForm.constellation" placeholder="请输入星座"></el-input>
            </el-form-item>
            <el-form-item label="作息时间">
                <el-input v-model="profileForm.schedule" placeholder="请输入作息时间"></el-input>
            </el-form-item>
            <el-form-item label="是否抽烟">
                <el-switch v-model="profileForm.smoke"></el-switch>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm">提交</el-button>
                <el-button @click="resetForm">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script setup>
import { ref } from 'vue';

const profileForm = ref({
    gender: 1,
    region: '',
    constellation: '',
    schedule: '',
    smoke: true,
});

const handleChangeGender = (evnet) => {
    console.log(evnet);
}

const submitForm = () => {
    console.log('表单提交:', profileForm.value);
    // 这里可以添加你的提交逻辑，如API调用  
};

const resetForm = () => {

};  
</script>