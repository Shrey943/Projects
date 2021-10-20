package com.example.credence;

import android.annotation.SuppressLint;
import android.app.Fragment;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.ItemTouchHelper;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.credence.adapter.RecyclerViewAdapter;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static android.content.Context.MODE_PRIVATE;

public class Fragment2 extends Fragment {
     RecyclerView recyclerView;
    RecyclerViewAdapter recyclerViewAdapter;
    ArrayList<model> beliefArrayList;


    @SuppressLint("ResourceAsColor")
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment2_layout,container,false);


        recyclerView = view.findViewById(R.id.recyclerView);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        beliefArrayList = new ArrayList<>();
        int a = 1;

        SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);

        if (shrd.getBoolean("my_first_time",true)) {

        }

        else {

            int n = shrd.getInt("id", 1);
            while (a<n) {

                String belief  = shrd.getString("belief"+a,"");
                float per = shrd.getFloat("per"+a,(float)25.55);

                model model = new model();
                model.setBelief(belief);
                model.setPer(per);

                beliefArrayList.add(model);

//               LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT);
//               LinearLayout.LayoutParams params3 = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT);
//               LinearLayout.LayoutParams params4 = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT);
//               params4.weight = 0.8f;
//               params.weight = 0.8f;
//               params3.weight = 2.5f;


//
//                params.setMargins(10,10,10,10);
//
//                TextView credence = new TextView(getContext());
//                credence.setLayoutParams(params3);
//                credence.setText(belief);
//                credence.setGravity(Gravity.CENTER_VERTICAL);
//                credence.setTextSize(13);
//                credence.setPadding(10,0,0,0);
//                credence.setTextColor(getResources().getColor(R.color.white));
//
//
//                TextView credence2 = new TextView(getContext());
//                credence2.setLayoutParams(params4);
//                credence2.setText("| "+ per + "% |");
//                credence2.setTextSize(15);
//                credence2.setGravity(Gravity.CENTER);
//                credence2.setTextColor(getResources().getColor(R.color.white));
//
//
//               Button update = new Button(getContext());
//               update.setLayoutParams(params);
//               update.setId(a);
//
//               update.setText("UPDATE");
//               update.setBackgroundColor(android.R.color.transparent);
//
//               update.setTextColor(getResources().getColor(R.color.grey));
//               update.setGravity(Gravity.CENTER);
//               update.setTextSize(15);
//               update.setOnClickListener(new View.OnClickListener() {
//                   @Override
//                   public void onClick(View view) {
//
//                       Intent intent = new Intent(getActivity(), EditActivity.class);
//                       int id = view.getId();
//                       intent.putExtra("ID",String.valueOf(id));
//                       startActivity(intent);
//
//                   }
//               });
//
//                LinearLayout.LayoutParams params2 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
//                params2.setMargins(20,5,20,5);
//
//
//                LinearLayout linearLayoutH = new LinearLayout(getContext());
//                linearLayoutH.setOrientation(LinearLayout.HORIZONTAL);
//                linearLayoutH.setLayoutParams(params2);
//                linearLayoutH.setBackgroundResource(R.color.demand);
//                linearLayoutH.addView(credence);
//                linearLayoutH.addView(credence2);
//
//                linearLayoutH.addView(update);
//
//
//                credences.addView(linearLayoutH);
                a=a+1;

            }
            recyclerViewAdapter = new RecyclerViewAdapter(getActivity(),beliefArrayList);
            recyclerView.setAdapter(recyclerViewAdapter);

            ItemTouchHelper itemTouchHelper = new ItemTouchHelper(simpleCallback);
            itemTouchHelper.attachToRecyclerView(recyclerView);


        }
        return view;

    }
    ItemTouchHelper.SimpleCallback simpleCallback = new ItemTouchHelper.SimpleCallback(ItemTouchHelper.UP | ItemTouchHelper.DOWN | ItemTouchHelper.START | ItemTouchHelper.END,0) {
        @Override
        public boolean onMove(@NonNull RecyclerView recyclerView, @NonNull RecyclerView.ViewHolder viewHolder, @NonNull RecyclerView.ViewHolder target) {

            int fromPosition = viewHolder.getAdapterPosition();
            int toPosition = target.getAdapterPosition();

            Collections.swap(beliefArrayList,fromPosition,toPosition);

            recyclerView.getAdapter().notifyItemMoved(fromPosition,toPosition);

            if(fromPosition>toPosition) {
                SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);
                int from = fromPosition + 1;
                int to = toPosition + 1;
//            String from_belief = shrd.getString("belief"+(from),"");
//            float from_per = shrd.getFloat("per"+(from),0.0f);
//            String from_comment = shrd.getString("comment"+from,"");
//            String to_belief = shrd.getString("belief"+(to),"");
//            float to_per = shrd.getFloat("per"+(to),0.0f);
//            String to_comment = shrd.getString("comment"+to,"");
                SharedPreferences.Editor editor = shrd.edit();

                String belief = shrd.getString("belief" + to, "");
                float per = shrd.getFloat("per" + to, 0f);
                String comment = shrd.getString("comment" + to, "");
                editor.putString("belief" + 0, belief);
                editor.putFloat("per" + 0, per);
                editor.putString("comment" + 0, comment);
                editor.apply();

                while (to < from) {

                    String belief1 = shrd.getString("belief" + 0, "");
                    float per1 = shrd.getFloat("per" + 0, 0f);
                    String comment1 = shrd.getString("comment" + 0, "");

                    String belief2 = shrd.getString("belief" + (to + 1), "");
                    float per2 = shrd.getFloat("per" + (to + 1), 0f);
                    String comment2 = shrd.getString("comment" + (to + 1), "");

                    SharedPreferences.Editor editor1 = shrd.edit();
                    editor1.putString("belief" + (to + 1), belief1);
                    editor1.putFloat("per" + (to + 1), per1);
                    editor1.putString("comment" + (to + 1), comment1);
                    editor1.putString("belief" + 0, belief2);
                    editor1.putFloat("per" + 0, per2);
                    editor1.putString("comment" + 0, comment2);
                    editor1.apply();
                    to = to + 1;
                }
                String belief1 = shrd.getString("belief" + 0, "");
                float per1 = shrd.getFloat("per" + 0, 0f);
                String comment1 = shrd.getString("comment" + 0, "");
                SharedPreferences.Editor editor1 = shrd.edit();
                editor1.putString("belief" + (toPosition + 1), belief1);
                editor1.putFloat("per" + (toPosition + 1), per1);
                editor1.putString("comment" + (toPosition + 1), comment1);
                editor1.apply();
            }
            else if(toPosition>fromPosition){
                SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);
                int from = fromPosition + 1;
                int to = toPosition + 1;
//            String from_belief = shrd.getString("belief"+(from),"");
//            float from_per = shrd.getFloat("per"+(from),0.0f);
//            String from_comment = shrd.getString("comment"+from,"");
//            String to_belief = shrd.getString("belief"+(to),"");
//            float to_per = shrd.getFloat("per"+(to),0.0f);
//            String to_comment = shrd.getString("comment"+to,"");
                SharedPreferences.Editor editor = shrd.edit();

                String belief = shrd.getString("belief" + to, "");
                float per = shrd.getFloat("per" + to, 0f);
                String comment = shrd.getString("comment" + to, "");
                editor.putString("belief" + 0, belief);
                editor.putFloat("per" + 0, per);
                editor.putString("comment" + 0, comment);
                editor.apply();

                while (from < to) {

                    String belief1 = shrd.getString("belief" + 0, "");
                    float per1 = shrd.getFloat("per" + 0, 0f);
                    String comment1 = shrd.getString("comment" + 0, "");

                    String belief2 = shrd.getString("belief" + (to - 1), "");
                    float per2 = shrd.getFloat("per" + (to - 1), 0f);
                    String comment2 = shrd.getString("comment" + (to - 1), "");

                    SharedPreferences.Editor editor1 = shrd.edit();
                    editor1.putString("belief" + (to - 1), belief1);
                    editor1.putFloat("per" + (to - 1), per1);
                    editor1.putString("comment" + (to - 1), comment1);
                    editor1.putString("belief" + 0, belief2);
                    editor1.putFloat("per" + 0, per2);
                    editor1.putString("comment" + 0, comment2);
                    editor1.apply();
                    from = from + 1;
                }
                String belief1 = shrd.getString("belief" + 0, "");
                float per1 = shrd.getFloat("per" + 0, 0f);
                String comment1 = shrd.getString("comment" + 0, "");
                SharedPreferences.Editor editor1 = shrd.edit();
                editor1.putString("belief" + (toPosition + 1), belief1);
                editor1.putFloat("per" + (toPosition + 1), per1);
                editor1.putString("comment" + (toPosition + 1), comment1);
                editor1.apply();
            }
            else {}


            return false;
        }

        @Override
        public void onSwiped(@NonNull RecyclerView.ViewHolder viewHolder, int direction) {

        }
    };


}


















