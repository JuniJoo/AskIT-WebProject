<template>
    <div class=" dark:bg-gray-900 bg-sky-100 h-full">
        <div class="md:mx-auto md:w-10/12 md:max-w-6xl dark:bg-gray-800 overflow-hidden bg-white shadow-lg">
            <div class="flex items-center sm:w-full p-4">
                <div class="flex flex-col items-center">
                    <button
                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 mr-2 rounded bg-green-500 px-2 py-1 font-bold text-white hover:bg-green-600"
                            :class="{ ' border-4 border-green-600': question.upvote_or_downvote === 'upvote'}"
                            v-on:click="upvoteQuestion">
                        <i class="fa fa-arrow-up"></i>
                    </button>
                    <span class="mr-2 text-lg font-bold dark:text-white text-gray-600">{{ question.score }}</span>
                    <button
                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 mr-2 rounded bg-red-500 px-2 py-1 font-bold text-white hover:bg-red-600"
                            :class="{ ' border-4 border-red-600': question.upvote_or_downvote === 'downvote'}"
                            v-on:click="downvoteQuestion">
                        <i class="fa fa-arrow-down"></i>
                    </button>
                </div>

                <div class="flex-grow w-1">
                    <div class="flex justify-between items-center mb-2">
                        <h1 class="p-2 font-mono text-3xl font-bold">{{ question.title }}</h1>
                        <!-- <p>hello there {{ user.username }} </p> -->
                        <div class="relative inline-block text-left">
                            <button v-if="user.username === question.author"
                                    class="transition  focus:outline-none  mt-3 mr-2 mb-2 rounded-lg bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-pink-400"
                                    type="button"
                                    @click="toggleDropdown"
                            >
                                <span>Options</span>
                            </button>

                            <div
                                    class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-100"
                                    v-show="showDropdown"
                            >
                                <div class="py-1">

<!--                                    <button-->
<!--                                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 flex justify-start w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900"-->
<!--                                            @click="editItem">-->
<!--                                        <svg style="color: blue" xmlns="http://www.w3.org/2000/svg" width="20"-->
<!--                                             height="20"-->
<!--                                             fill="currentColor" class="mr-3 bi bi-pencil" viewBox="0 0 16 16">-->
<!--                                            <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0-->
<!--          1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0-->
<!--          1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"-->
<!--                                                  fill="blue"></path>-->
<!--                                        </svg>-->
<!--                                        Edit-->
<!--                                    </button>-->

                                    <button v-on:click="deleteQuestion"
                                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 flex justify-start w-full px-4 py-2 text-sm text-red-700 hover:bg-gray-100 hover:text-red-900">
                                        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                  d="M6 18L18 6M6 6l12 12"/>
                                        </svg>
                                        Delete
                                    </button>

<!--                                    <button v-on:click="muteNotifications"-->
<!--                                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 flex justify-start w-full px-4 py-2 text-sm text-black hover:bg-gray-100 hover:text-black">-->
<!--                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"-->
<!--                                             fill="currentColor"-->
<!--                                             class="mr-3 bi bi-bell" viewBox="0 0 16 16">-->
<!--                                            <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zM8 1.918l-.797.161A4.002 4.002 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376-->
<!--            1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4.002 4.002 0 0 0-3.203-3.92L8 1.917zM14.22-->
<!--            12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5.002 5.002 0 0-->
<!--            1 13 6c0 .88.32 4.2 1.22 6z"/>-->
<!--                                        </svg>-->
<!--                                        Mute Notifications-->
<!--                                    </button>-->
                                </div>
                            </div>
                        </div>


                        <!-- <div class="relative">
                          <button @click="toggleMenu"
                                  class=" justify-between mr-20 px-4 py-2 rounded-md border-2 border-gray-300 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                            Options
                          </button>
                          <div v-show="showMenu"
                              class=" justify-between mr-20 placeholder:absolute z-10 w-56 mt-2  bg-white border border-gray-200 divide-y divide-gray-100 rounded-md shadow-lg">
                            <button class="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900">
                              Option 1
                            </button>
                            <button class="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900">
                              Option 2
                            </button>
                          </div>
                        </div> -->
                        <!-- <button    v-on:click="deleteQuestion" type="button"
                                  class="justify-between rounded-lg bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300">
                            Delete Question
                            v-if=" question.author = 'adinotadmin@mail.com' "
                        </button> -->
                    </div>
                    <div class="mb-2 flex justify-between">
                        <p class="p-2 font-sans font-thin w-full">Author: {{ question.author }}</p>
                        <span class="w-full text-right dark:text-white text-gray-600">Date Published: {{
                            formatPubDate(question.pub_date)
                            }}</span>
                    </div>
                    <div>
                        <span class="font-bold">Explanation:</span>
                        <br>
                        <div class="mb-2 p-2 break-words border border-gray-200 dark:border-gray-600 rounded-md">

                            <div class="prose prose-headings:m-1 prose-p:m-1 prose-hr:m-1 dark:prose-invert"
                                 :class="{ 'prose-lg': largeText }"
                                 v-html="question.explanationHTML"></div>
                        </div>
                        <span class="font-bold">Tried what:</span> <br>
                        <div class="mb-2 p-2 break-words border border-gray-200 dark:border-gray-600 rounded-md">
                            <div class="prose prose-sm prose-headings:m-1 prose-p:m-1 prose-hr:m-1 dark:prose-invert"
                                 :class="{ 'prose-lg': largeText }"
                                 v-html="question.tried_whatHTML"></div>
                        </div>
                        <p class="mb-2 p-2 break-words"><span class="font-bold">Summary:</span> <br>
                            {{ question.summary }}
                        </p>
                        <div class="flex">
                            <div v-for="tag in question.tags" class="mr-2">
                                <button
                                        class="transition focus:ring-4 focus:outline-none dark:bg-indigo-900 dark:text-white focus:ring-blue-400 rounded bg-blue-50 px-2 py-1 text-blue-400 hover:bg-blue-100">
                                    {{ tag }}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="flex justify-center px-2">
                <br>
            </div>

            <div class="p-5">
                <div class="flex items-center">
                    <h1 class="font-bold">Comments:</h1>
                    <button
                            class="transition focus:ring-4 focus:outline-none dark:bg-blue-600 dark:text-white focus:ring-blue-400 ml-4 rounded border-gray-300 bg-blue-100 px-4 py-1 font-sans font-bold text-black hover:bg-blue-300"
                            @click="showComments = !showComments">Add Comment
                    </button>
                </div>
                <div v-if="showComments" class="flex justify-center p-2">
                    <form @submit.prevent="addComment" class="w-5/6">
                        <br>
                        <div>
                            <textarea v-model="commentInput"
                                      class="transition focus:ring-2 focus:outline-none  block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:text-white h-24">
                            </textarea>
                        </div>
                        <br>
                        <button
                                class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 ml-4 rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-600"
                                type="submit">
                            Submit
                        </button>
                    </form>
                </div>
                <br>
                <div v-if="all_comments.length === 0"
                     class="mb-4 flex items-center rounded-lg dark:text-black dark:bg-blue-100 p-2 shadow">
                    <p class="dark:text-black">No comments yet.</p>
                </div>

                <div v-for="com in all_comments" :key="com.id">
                    <div class="flex mb-4 items-center rounded-lg dark:bg-gray-900 bg-white py-1 px-2 shadow">
                        <div class="w-full">
                            <div class="flex justify-between">
                                <p class="text-sm truncate dark:text-gray-300 text-gray-600">Author: {{ com.author }} </p>
                                <p class="text-right text-sm dark:text-gray-300 text-gray-600">Published: {{
                                    formatPubDate(com.pub_date)
                                    }}</p>
                            </div>
                            <div class="flex items-center justify-between">
                                <p v-if="com.is_solution" class="mt-2 text-sm font-semibold text-green-500">
                                    Solution</p>
                                <!--                                <p class="text-lg" style="word-break: break-word">{{ com.content }}</p>-->
                                <div class="w-full prose prose-sm prose-headings:m-1 prose-p:m-1 prose-hr:m-1 dark:prose-invert prose-p:break-words"
                                     v-html="com.contentHTML" :class="{ 'prose-lg': largeText, 'prose-sm': !largeText }"></div>
                                <button v-if="user.username == com.author" v-on:click="deleteComment(com.id)"
                                        class="transition focus:ring-4 focus:outline-none focus:ring-pink-400 bg-blue-600 hover:bg-blue-700 text-white text-sm rounded-md">
                                    Delete comment
                                </button>
                            </div>
                        </div>
                    </div>
                </div>


            </div>

            <div class="flex justify-center px-2">
                <button
                        class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 ml-4 w-5/6 rounded border-gray-300 bg-blue-100 px-4 py-2 font-sans font-bold text-black hover:bg-blue-300 dark:bg-blue-700 dark:text-white"
                        @click="showForm = !showForm">Answer this question
                </button>
            </div>
            <div v-if="showForm" class="flex justify-center p-2">
                <form @submit.prevent="addAnswer" class="w-5/6">
                    <br>
                    <div>
                        <textarea v-model="answerInput"
                                  class="transition focus:ring-2 focus:outline-none  block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:text-white h-48">
                        </textarea>
                    </div>
                    <br>
                    <button
                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 ml-4 rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-600"
                            type="submit">
                        Submit answer
                    </button>
                </form>
            </div>
            <div class="p-5">
                <h1 class="mb-4 text-2xl font-bold">Answers:</h1>

                <div v-if="answers.length === 0"
                     class="mb-4 flex items-center rounded-lg dark:bg-blue-100 dark:text-black bg-white p-4 shadow">
                    <p class="text-lg">No answers yet. Be the first to answer this question!</p>
                </div>

                <div v-for="answer in answers" :key="answer.id">
                    <div class="mb-4 flex items-center rounded-lg dark:bg-gray-900 bg-white p-4 shadow">
                        <div class="flex flex-col items-center">
                            <button
                                    class=" transition focus:ring-4 focus:outline-none focus:ring-blue-400mr-2 rounded bg-green-500 px-2 py-1 font-bold text-white hover:bg-green-600"
                                    :class="{ ' border-4 border-green-600': answer.upvote_or_downvote === 'upvote' }"
                                    v-on:click="upvoteAnswer(answer.id)">
                                <i class="fa fa-arrow-up"></i>
                            </button>
                            <span class="mr-2 text-lg font-bold dark:text-white text-gray-600">{{
                                answer.score
                                }}</span>
                            <button
                                    class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 mr-2 rounded bg-red-500 px-2 py-1 font-bold text-white hover:bg-red-600"
                                    :class="{ ' border-4 border-red-600': answer.upvote_or_downvote === 'downvote' }"
                                    v-on:click="downvoteAnswer(answer.id)">
                                <i class="fa fa-arrow-down"></i>
                            </button>
                        </div>
                        <div class="flex-grow w-11/12">
                            <div class="flex justify-between">
                                <p class="text-sm truncate dark:text-gray-300 text-gray-600">Author: {{ answer.author }} </p>
                                <p class="text-right text-sm dark:text-gray-300 text-gray-600">Published:
                                    {{ formatPubDate(answer.pub_date) }}</p>
                            </div>
                            <div class="flex items-center justify-between">
                                <p v-if="answer.is_solution" class="mt-2 text-sm font-semibold text-green-500">
                                    Solution
                                </p>
                                <p v-if="answer.from_admin" class="mt-2 text-sm font-semibold text-green-500">
                                    From admin
                                </p>
                                <!--                                <p class="text-lg" style="word-break: break-word;">{{ answer.content }}</p>-->
                                <div class="w-full prose prose-headings:m-1 prose-p:m-1 prose-hr:m-1 dark:prose-invert prose-p:break-words"
                                     v-html="answer.contentHTML" :class="{ 'prose-lg': largeText, 'prose-sm': !largeText }"></div>

                                <div>
                                    <button v-if="user.username === answer.author"
                                            class="transition  focus:outline-none mt-3 mr-2 mb-2 rounded-lg bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-pink-400"
                                            type="button"
                                            @click="toggleAnswerDropdown(answer)">
                                        <span>Options</span>
                                    </button>

                                    <div
                                            class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-100"
                                            v-show="answer.showDropdown">
                                        <div class="py-1">

<!--                                            <button @click="editItem"-->
<!--                                                    class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 flex justify-start w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900"-->
<!--                                            >-->
<!--                                                <svg style="color: blue" xmlns="http://www.w3.org/2000/svg"-->
<!--                                                     width="20"-->
<!--                                                     height="20"-->
<!--                                                     fill="currentColor" class="mr-3 bi bi-pencil"-->
<!--                                                     viewBox="0 0 16 16">-->
<!--                                                    <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0-->
<!--                    1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0-->
<!--                    1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"-->
<!--                                                          fill="blue"></path>-->
<!--                                                </svg>-->
<!--                                                Edit Answer-->
<!--                                            </button>-->

                                            <button v-on:click="deleteAnswer(answer.id)"
                                                    class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 flex justify-start w-full px-4 py-2 text-sm text-red-700 hover:bg-gray-100 hover:text-red-900">
                                                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor"
                                                     viewBox="0 0 24 24"
                                                     xmlns="http://www.w3.org/2000/svg">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                          stroke-width="2"
                                                          d="M6 18L18 6M6 6l12 12"/>
                                                </svg>
                                                Delete Answer
                                            </button>

<!--                                            <button v-on:click="muteNotifications"-->
<!--                                                    class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 flex justify-start w-full px-4 py-2 text-sm text-black hover:bg-gray-100 hover:text-black">-->
<!--                                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"-->
<!--                                                     fill="currentColor"-->
<!--                                                     class="mr-3 bi bi-bell" viewBox="0 0 16 16">-->
<!--                                                    <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zM8 1.918l-.797.161A4.002 4.002 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376-->
<!--                      1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4.002 4.002 0 0 0-3.203-3.92L8 1.917zM14.22-->
<!--                      12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5.002 5.002 0 0-->
<!--                      1 13 6c0 .88.32 4.2 1.22 6z"/>-->
<!--                                                </svg>-->
<!--                                                Mute Notifications-->
<!--                                            </button>-->
                                        </div>
                                    </div>
                                    <div v-if="user.username === question.author"
                                         class="flex items-center justify-between">
                                        <button
                                                class="transition focus:outline-none mt-3 mr-2 mb-2 rounded-lg bg-green-600 px-4 text-sm font-medium text-white py-2 hover:bg-green-500 focus:ring-4 focus:ring-pink-400"
                                                type="button"
                                                @click="markAsSolution(answer.id)">
                                            <span>Mark as solution</span>
                                        </button>


                                    </div>
                                </div>


                                <!-- <button v-if="user.username == answer.author" class="mt-3 mr-2 mb-2 rounded-lg bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300"
                            v-on:click="deleteAnswer(answer.id)">
                                Delete Answer
                            </button> -->
                            </div>
                        </div>
                    </div>

                </div>

            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";
import { marked } from "marked";
import * as DOMPurify from "dompurify";

export default {
    name: "QuestionView",
    data() {
        return {
            showForm: false,
            showComments: false,
            showDropdown: false,
            showDropdownAnswers: false,
            user: {},

            question: {
                title: "Loading...",
                explanation: "Loading...",
                tried_what: "Loading...",
                summary: "Loading...",
                pub_date: "2000-01-01T00:00:00Z",
                explanationHTML: "# markdown",
                tried_whatHTML: "# markdown",

            },
            answers: [],
            answerInput: "",
            all_comments: [],
            commentInput: "",
            moduleTitle: "",
            largeText: false,
        };
    },
    mounted() {
        axiosClient({
            method: "get",
            url: `/question/${this.$route.params.id}/`,
        })
            .then((response) => {
                this.question = response.data;
                this.answers = response.data.answer_list.sort((a, b) => b.score - a.score);
                for (let answer of this.answers) {
                    answer.contentHTML = DOMPurify.sanitize(marked(answer.content));
                }
                this.all_comments = response.data.comment_list;
                for (let comment of this.all_comments) {
                    comment.contentHTML = DOMPurify.sanitize(marked(comment.content));
                }
                this.module = response.data.module;
                this.question.explanationHTML = DOMPurify.sanitize(marked(this.question.explanation));
                this.question.tried_whatHTML = DOMPurify.sanitize(marked(this.question.tried_what));
            })
            .catch((error) => {
                console.log(error);
            });

        axiosClient.get('/v1/users/me').then(response => {
            this.user = response.data
        }).catch(error => {
            console.log(error)
        })

        if (localStorage.getItem("largeFont") === "true") {
            this.largeText = true;
        }
    },


    methods: {
        markAsSolution(answer_id) {
            axiosClient.post(`/question/${this.$route.params.id}/accept_answer/${answer_id}/`)
                .then((response) => {
                    window.location.reload();
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },

        toggleAnswerDropdown(answer) {
            answer.showDropdown = !answer.showDropdown;
        },
        addAnswer() {
            console.log(this.answerInput)
            axiosClient.post(`/question/${this.$route.params.id}/submit_answer/`,
                {
                    content: this.answerInput,
                })
                .then((response) => {
                    const answer = response.data;
                    answer.contentHTML = DOMPurify.sanitize(marked(answer.content));
                    this.answers.push(answer);
                    this.answerInput = "";
                    this.showForm = false;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        addComment() {
            console.log(this.commentInput)
            axiosClient.post(`/question/${this.$route.params.id}/submit_comment/`,
                {
                    content: this.commentInput,
                })
                .then((response) => {
                    let comment = response.data;
                    comment.contentHTML = DOMPurify.sanitize(marked(comment.content));
                    this.all_comments.push(comment);
                    this.commentInput = "";
                    this.showComments = false;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        deleteComment(comId) {
            axiosClient.delete(`/question/${this.$route.params.id}/comment/${comId}/delete_comment/`)
                .then((response) => {
                    // window.location.href = `/question/${this.$route.params.id}`;
                    this.all_comments = this.all_comments.filter(comment => comment.id !== comId);
                })
                .catch((error) => {
                    console.log(error);
                });

        },

        deleteAnswer(answerId) {
            if (!confirm("Are you sure you want to delete this answer?")) {
                return;
            }
            axiosClient.delete(`/question/${this.$route.params.id}/answer/${answerId}/delete_answer/`)
                .then((response) => {
                    window.location.href = `/question/${this.$route.params.id}`;
                })
                .catch((error) => {
                    console.log(error);
                });
        },


        upvoteQuestion() {
            axiosClient.post(`/question/${this.$route.params.id}/upvote/`)
                .then((response) => {
                    this.question.score = response.data.score;
                    if (response.data.success) {
                        this.question.upvote_or_downvote = "upvote";
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        downvoteQuestion() {
            axiosClient.post(`/question/${this.$route.params.id}/downvote/`)
                .then((response) => {
                    this.question.score = response.data.score;
                    if (response.data.success) {
                        this.question.upvote_or_downvote = "downvote";
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        upvoteAnswer(answerId) {
            axiosClient.post(`/question/${this.$route.params.id}/answer/${answerId}/upvote/`)
                .then((response) => {
                    this.answers = this.answers.map((answer) => {
                        if (answer.id === answerId) {
                            answer.score = response.data.score;
                            if (response.data.success) {
                                answer.upvote_or_downvote = "upvote";
                            }
                        }
                        return answer;
                    }).sort((a, b) => b.score - a.score);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        downvoteAnswer(answerId) {
            axiosClient.post(`/question/${this.$route.params.id}/answer/${answerId}/downvote/`)
                .then((response) => {
                    this.answers = this.answers.map((answer) => {
                        if (answer.id === answerId) {
                            answer.score = response.data.score;
                            if (response.data.success) {
                                answer.upvote_or_downvote = "downvote";
                            }
                        }
                        return answer;
                    }).sort((a, b) => b.score - a.score);
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        deleteQuestion() {
            if (window.confirm("Are you sure you want to delete this question?") === false) {
                return;
            }
            axiosClient.delete(`/question/${this.$route.params.id}/delete/`)
                .then((response) => {
                    window.location.href = `/module/${response.data.module}`;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>
<script setup>
import { formatPubDate } from "./dateUtils";

</script>

<style scoped>

</style>
