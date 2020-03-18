import os
import numpy as np
import sys


def split_frames(data_root, split_length=32, max_frame=300):
    # e.g. data_root = '/root/bpe-dev/unity/dataset/Original'
    # e.g. if max_frame = 300, SARA is splitted under the 300 frames
    # if max_frame is set to None, this function split all motion frames

    for phase in ['train', 'test']:
        phase_dir = os.path.join(data_root, phase)
        character_names = os.listdir(phase_dir)

        for char in character_names:
            char_dir = os.path.join(phase_dir, char)
            animation_names = os.listdir(char_dir)

            for anim in animation_names:
                variation_p_dir = os.path.join(char_dir, anim)
                variations_len = os.listdir(variation_p_dir)

                for var_len in variations_len:
                    var_path = os.path.join(variation_p_dir, var_len)
                    var_list = os.listdir(var_path)
                    for var in var_list:
                        motion_path = os.path.join(var_path, var, 'motion.npy')
                        animation = np.load(motion_path)
                        total_length = animation.shape[-1]
                        if total_length < split_length:
                            continue
                        mot_dir = os.path.join(var_path, var, 'motions')
                        if not os.path.exists(mot_dir):
                            os.makedirs(mot_dir)
                        nr_motions = total_length // (split_length // 2) - 1
                        for i in range(nr_motions):
                            if max_frame is not None and i * (split_length // 2) + split_length > max_frame:
                                break
                            save_path = os.path.join(mot_dir, '{}.npy'.format(i + 1))
                            window = animation[:, :, i * (split_length // 2): i * (split_length // 2) + split_length]
                            np.save(save_path, window)
                            print(save_path, window.shape)


if __name__ == '__main__':
    
    data_root = sys.argv[1]  # data_root : /path/to/SARA_released/
    
    split_frames(data_root)
    