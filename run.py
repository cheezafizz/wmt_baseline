import os
os.environ['model_name'] = 'Helsinki-NLP/opus-mt-en-fr'
os.environ['data_path'] = 'data_2_terminology'
os.environ['output_dir'] = 'use_terms'


os.environ['batch_size'] = '32'
os.environ['eval_batch_size'] = '64'
os.environ['max_length'] = '128'
os.environ['n_epochs'] = '3'

os.environ['max_samples'] = '9999999'

os.system("python3 baseline_hf.py --model_name_or_path $model_name \
                                --output_dir $output_dir \
                                --data_path $data_path \
                                --do_train \
                                --do_eval \
                                --do_predict \
                                --load_best_model_at_end \
                                --metric_for_best_model 'bleu' \
                                --greater_is_better true \
                                --predict_with_generate \
                                --fp16 \
                                --evaluation_strategy 'epoch' \
                                --learning_rate 2e-5 \
                                --per_device_train_batch_size $batch_size \
                                --per_device_eval_batch_size $eval_batch_size \
                                --max_source_length $max_length \
                                --max_target_length $max_length \
                                --weight_decay=0.01 \
                                --save_total_limit 3 \
                                --num_train_epochs $n_epochs \
                                --max_train_samples $max_samples")
